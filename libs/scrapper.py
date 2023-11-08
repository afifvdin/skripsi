import json, html, pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from snscrape.base import ScraperException
from snscrape.modules.twitter import (
    Tweet,
    _TwitterAPIType,
    TwitterTweetScraper,
    TwitterTweetScraperMode,
)
from libs.config import ScrapperConfig


def get_items(self):
    variables = {
        "tweetId": str(self._tweetId),
        "includePromotedContent": True,
        "withCommunity": True,
        "withVoice": True,
        # !!! these fields may be deprecated
        # "with_rux_injections": False,
        # "withQuickPromoteEligibilityTweetFields": True,
        # "withBirdwatchNotes": False,
        # "withV2Timeline": True,
    }
    features = {
        "responsive_web_graphql_exclude_directive_enabled": True,
        "verified_phone_label_enabled": False,
        "creator_subscriptions_tweet_preview_api_enabled": False,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
        "tweetypie_unmention_optimization_enabled": True,
        "responsive_web_edit_tweet_api_enabled": True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
        "view_counts_everywhere_api_enabled": True,
        "longform_notetweets_consumption_enabled": True,
        "tweet_awards_web_tipping_enabled": False,
        "freedom_of_speech_not_reach_fetch_enabled": True,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
        "longform_notetweets_rich_text_read_enabled": True,
        "longform_notetweets_inline_media_enabled": False,
        "responsive_web_enhance_cards_enabled": False,
        "responsive_web_twitter_article_tweet_consumption_enabled": False,  # new?
        "responsive_web_media_download_video_enabled": True,  # new?
        # !!! these fields may be deprecated
        # "rweb_lists_timeline_redesign_enabled": False,
        # "vibe_api_enabled": True,
        # "interactive_text_enabled": True,
        # "blue_business_profile_image_shape_enabled": True,
        # "responsive_web_text_conversations_enabled": False,
    }
    fieldToggles = {
        "withArticleRichContentState": True,
        "withAuxiliaryUserLabels": True,
    }
    params = {
        "variables": variables,
        "features": features,
        "fieldToggles": fieldToggles,  # seems optional
    }
    url = "https://twitter.com/i/api/graphql/3HC_X_wzxnMmUBRIn3MWpQ/TweetResultByRestId"
    try:
        if self._mode is TwitterTweetScraperMode.SINGLE:
            obj = self._get_api_data(url, _TwitterAPIType.GRAPHQL, params=params)
            if not obj["data"]["tweetResult"]:
                return
            yield self._graphql_timeline_tweet_item_result_to_tweet(
                obj["data"]["tweetResult"]["result"], tweetId=self._tweetId
            )
    except:
        return


TwitterTweetScraper.get_items = get_items


class Scrapper:
    def __init__(self, config: ScrapperConfig) -> None:
        self.config = config

    def get_urls(self):
        ################## OPTIONS
        ffOptions = Options()
        ffOptions.add_argument("-profile")
        ffOptions.add_argument(self.config.FIREFOX_PROFILE_PATH)
        geckodriver_path = "/snap/bin/geckodriver"
        driver_service = Service(executable_path=geckodriver_path)
        driver = webdriver.Firefox(service=driver_service, options=ffOptions)
        ################## GLOBAL VARS
        res = set()
        MINIMUM_TWEETS = self.config.MINIMUM_TWEETS
        SHORT_TIMEOUT = self.config.SHORT_TIMEOUT
        LONG_TIMEOUT = self.config.LONG_TIMEOUT
        LOADING_ELEMENT_XPATH = "//div[@role='progressbar']"

        pbar = tqdm(
            total=self.config.MINIMUM_TWEETS,
            bar_format="[Tweet link] {desc} [{bar:30}]",
            ascii=".>=",
        )

        for URL in self.config.EXPLORE_URLS:
            pbar.set_description(f"{len(res)}/{self.config.MINIMUM_TWEETS}")
            driver.get(URL)
            for i in range(20):
                try:
                    WebDriverWait(driver, SHORT_TIMEOUT).until(
                        EC.presence_of_element_located(
                            (By.XPATH, LOADING_ELEMENT_XPATH)
                        )
                    )
                    WebDriverWait(driver, LONG_TIMEOUT).until_not(
                        EC.presence_of_element_located(
                            (By.XPATH, LOADING_ELEMENT_XPATH)
                        )
                    )
                except TimeoutException:
                    pass
                count = 0
                links = driver.find_elements(
                    by=By.XPATH, value="//a[@role='link' and @dir='ltr']"
                )
                for link in links:
                    try:
                        url = link.get_attribute("href")
                        if len(url.split("/")) == 6 and url not in res:
                            count += 1
                            res.add(url)
                            pbar.set_description(
                                f"{len(res)}/{self.config.MINIMUM_TWEETS}"
                            )
                            pbar.update(n=1)
                            if len(res) >= MINIMUM_TWEETS:
                                break
                            # print(url)
                    except:
                        pass
                if len(res) >= MINIMUM_TWEETS:
                    break
                if count == 0:
                    break
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        obj = json.dumps(list(res))
        with open(self.config.TWITTER_URLS_PATH, "w") as outfile:
            outfile.write(obj)
        driver.quit()

    def get_using_snscrape(self, tweet_id: int) -> Tweet | None:
        try:
            for tweet in TwitterTweetScraper(tweet_id).get_items():
                return tweet
            return "No response from public API."
        except:
            return "Scraping failed."

    def get_dataset(self):
        URLS = json.load(open(self.config.TWITTER_URLS_PATH))
        tweets = []

        pbar = tqdm(
            total=len(URLS),
            bar_format="[Tweet dataset] {desc} [{bar:30}]",
            ascii=".>=",
        )

        for URL in URLS:
            pbar.set_description(f"{len(tweets)}/{len(URLS)}")
            tweet_id = URL.split("/")[-1]
            res = self.get_using_snscrape(tweet_id)

            if res == "No response from public API.":
                continue
            elif res == "Scraping failed.":
                continue
            try:
                tweet = [
                    res.user.username,
                    res.user.displayname,
                    str(res.date),
                    res.url,
                    html.unescape(res.renderedContent),
                ]
                tweets.append(tweet)
                pbar.set_description(f"{len(tweets)}/{len(URLS)}")
                pbar.update(n=1)

            except:
                pass

        tweets_dataset = pd.DataFrame(
            tweets, columns=["username", "name", "date", "url", "tweet"]
        )
        tweets_dataset.to_excel(self.config.TWITTER_DATASET_PATH)
