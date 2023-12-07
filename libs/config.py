class ScrapperConfig:
    def __init__(self) -> None:
        self.MINIMUM_TWEETS = 1000

        # web driver timeout for scrolling, it keeps scrolling
        # whenever the loader element exist
        self.SHORT_TIMEOUT = 1
        self.LONG_TIMEOUT = 30

        self.TWITTER_CRAWLED_URLS_PATH = "./dataset/twitter_crawled_urls.json"
        self.TWITTER_CRAWLED_DATASET_PATH = "./dataset/twitter_crawled_dataset.xlsx"

        # Place your firefox profile path here so you can use your login cookie
        # you can do that via Help -> More Troubleshooting Information
        # and look for "Profile Directory"
        self.FIREFOX_PROFILE_PATH = (
            "/home/afifvdin/snap/firefox/common/.mozilla/firefox/sipwhe3c.default"
        )

        # You can split your twitter url
        # since doom scrolling twitter doesn't works
        self.EXPLORE_URLS = [
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-01-31%20since%3A2019-01-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-02-28%20since%3A2019-02-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-03-31%20since%3A2019-03-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-04-30%20since%3A2019-04-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-05-31%20since%3A2019-05-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-06-30%20since%3A2019-06-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-07-31%20since%3A2019-07-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-08-31%20since%3A2019-08-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-09-30%20since%3A2019-09-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-10-31%20since%3A2019-10-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-11-30%20since%3A2019-11-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2019-12-31%20since%3A2019-12-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-01-31%20since%3A2020-01-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-02-29%20since%3A2020-02-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-03-31%20since%3A2020-03-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-04-30%20since%3A2020-04-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-05-31%20since%3A2020-05-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-06-30%20since%3A2020-06-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-07-31%20since%3A2020-07-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-08-31%20since%3A2020-08-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-09-30%20since%3A2020-09-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-10-31%20since%3A2020-10-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-11-30%20since%3A2020-11-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2020-12-31%20since%3A2020-12-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-01-31%20since%3A2021-01-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-02-28%20since%3A2021-02-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-03-31%20since%3A2021-03-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-04-30%20since%3A2021-04-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-05-31%20since%3A2021-05-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-06-30%20since%3A2021-06-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-07-31%20since%3A2021-07-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-08-31%20since%3A2021-08-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-09-30%20since%3A2021-09-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-10-31%20since%3A2021-10-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-11-30%20since%3A2021-11-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2021-12-31%20since%3A2021-12-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-01-31%20since%3A2022-01-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-02-28%20since%3A2022-02-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-03-31%20since%3A2022-03-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-04-30%20since%3A2022-04-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-05-31%20since%3A2022-05-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-06-30%20since%3A2022-06-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-07-31%20since%3A2022-07-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-08-31%20since%3A2022-08-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-09-30%20since%3A2022-09-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-10-31%20since%3A2022-10-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-11-30%20since%3A2022-11-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2022-12-31%20since%3A2022-12-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2023-01-31%20since%3A2023-01-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2023-02-28%20since%3A2023-02-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2023-03-31%20since%3A2023-03-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2023-04-30%20since%3A2023-04-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2023-05-31%20since%3A2023-05-01&src=typed_query",
            "https://twitter.com/search?q=teknologi%20lang%3Aid%20until%3A2023-06-30%20since%3A2023-06-01&src=typed_query",
        ]


class Config:
    def __init__(self) -> None:
        self.MODEL_DIR = "./models"
        self.TWITTER_DATASET_PATH = "./dataset/twitter_dataset.xlsx"
        self.DICTIONARY_PATH = "./dataset/dictionary.json"
        self.PRE_ANNOTATED_TWITTER_JSON_PATH = "./dataset/pre_annotated_twitter.json"
        self.ANNOTATED_TWITTER_JSON_PATH = "./dataset/annotated_twitter.json"
        self.EMBEDDING_VECTOR_SIZE = 300
        self.EMBEDDING_WINDOW = 5
        self.EMBEDDING_USE_SKIP_GRAM = 1
        self.EMBEDDING_EPOCHS = 1000
