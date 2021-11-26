import pickle
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import typer


def load_data(data_path):
    texts = []
    labels = []
    with open(data_path) as f:
        for line in f:
            item = json.loads(line)
            texts.append(item["text"])
            labels.append(item["label"])
    return texts, labels


def train(data_path, model_path):
    X, y = load_data(data_path)

    pipeline = Pipeline([("tfidf", TfidfVectorizer()), ("svm", SGDClassifier())])
    pipeline.fit(X, y)

    with open(model_path, "wb") as f:
        f.write(pickle.dumps(model_path))


if __name__ == "__main__":
    typer.run(train)
