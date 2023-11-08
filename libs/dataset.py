import re, json, pandas as pd
from typing import List


class Dataset:
    def __init__(self) -> None:
        self.dataset = []
        self.VOCAB = ["<PAD>", "<UNK>"]
        self.TAGS = ["<PAD>", "<UNK>"]
        self.MAX_LEN = 0
        self.NUM_DATA = 0

    def load(self, path: str) -> None:
        with open(path, "r") as file:
            self.dataset = json.load(file)
            self.build_meta()

    def build_meta(self) -> None:
        self.VOCAB = ["<PAD>", "<UNK>"]
        self.TAGS = ["<PAD>", "<UNK>"]
        self.MAX_LEN = 0
        for data in self.dataset:
            if len(data["word_tag"]) > self.MAX_LEN:
                self.MAX_LEN = len(data["word_tag"])
            for [word, tag] in data["word_tag"]:
                if word not in self.VOCAB:
                    self.VOCAB.append(word)
                if tag not in self.TAGS:
                    self.TAGS.append(tag)
        self.NUM_DATA = len(self.dataset)

    def get_dataframe(self) -> pd.DataFrame:
        df = pd.DataFrame()
        words = []
        tags = []
        for data in self.dataset:
            word = []
            tag = []
            for w, t in data["word_tag"]:
                word.append(w)
                tag.append(t)
            words.append(word)
            tags.append(tag)
        df["words"] = words
        df["tags"] = tags
        df.loc[len(df)] = [
            ["<UNK>", "<PAD>"],
            ["<UNK>", "<PAD>"],
        ]
        return df


class Preprocess:
    def __init__(self, dictionary_path: str) -> None:
        with open(dictionary_path, "r") as fp:
            self.dictionary = json.load(fp)

    def to_sentence(self, s: str) -> str:
        ns = s.lower()
        ns = re.sub(r"\s+", " ", ns)
        return ns

    def to_token(self, s: str) -> List[str]:
        ns = re.findall(
            r"[@#]\w+|\b(?:https?|\.ly|\.com)\S*\b|\w+(?:-\w+)?|[^\w\s]+", s
        )
        return [self.dictionary.get(word, word) for word in ns]
