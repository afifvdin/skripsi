import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import sys, getopt, time, json, pandas as pd
from libs import Scrapper, ScrapperConfig, Config, Preprocess

cfg = Config()


def __run_dataset_collector():
    start_time = time.time()

    scfg = ScrapperConfig()
    scrapper = Scrapper(config=scfg)

    print("\n### Collecting dataset")
    print("Getting URL")
    scrapper.get_urls()
    print("Building dataset")
    scrapper.get_dataset()

    print(f"Raw dataset saved in {cfg.TWITTER_DATASET_PATH}")
    end_time = time.time()
    print("Process finished in {:.2f} s".format(end_time - start_time))


def __run_preprocess():
    # Data preprocessing
    start_time = time.time()
    print("\n### Preparing dataset")

    twitter_dataset = pd.read_excel(cfg.TWITTER_DATASET_PATH)
    preprocess = Preprocess(dictionary_path=cfg.DICTIONARY_PATH)

    twitter_dataset["tweet"] = twitter_dataset["tweet"].apply(preprocess.to_sentence)
    twitter_dataset["token"] = twitter_dataset["tweet"].apply(preprocess.to_token)

    pre_annotated_tweets = []
    for tweet, token in zip(
        twitter_dataset["tweet"].values.tolist(),
        twitter_dataset["token"].values.tolist(),
    ):
        pre_annotated_tweets.append(
            {
                "sentence": tweet,
                "word_tag": [[word, "TAG"] for word in token],
            }
        )

    with open(cfg.PRE_ANNOTATED_TWITTER_JSON_PATH, "w") as fp:
        json.dump(pre_annotated_tweets, fp)

    print(f"Dataset saved in {cfg.PRE_ANNOTATED_TWITTER_JSON_PATH}")
    end_time = time.time()
    print("Process finished in {:.2f} s".format(end_time - start_time))


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "dpto", ["dataset", "preprocess"])
    for opt, arg in opts:
        if opt in ("-d", "--dataset"):
            __run_dataset_collector()
            sys.exit()
        elif opt in ("-p", "--preprocess"):
            __run_preprocess()
            sys.exit()
