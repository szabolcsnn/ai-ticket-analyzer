from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer


DEFAULT_TRAINING_DATA_PATH = Path("data") / "training_tickets.csv"


class TicketCategoryClassifier:
    def __init__(self, training_data_path=DEFAULT_TRAINING_DATA_PATH):
        self.training_data_path = Path(training_data_path)
        self.model = Pipeline(
            [
                ("vectorizer", TfidfVectorizer()),
                ("classifier", MultinomialNB()),
            ]
        )
        self.is_trained = False

    def train_and_evaluate(self):
        training_dataframe = self._load_training_dataframe()
        features = self._build_text_features(training_dataframe)
        labels = training_dataframe["category"]

        x_train, x_test, y_train, y_test = train_test_split(
            features,
            labels,
            test_size=0.3,
            random_state=42,
            stratify=labels,
        )

        self.model.fit(x_train, y_train)
        predictions = self.model.predict(x_test)
        self.is_trained = True

        return {
            "accuracy": round(accuracy_score(y_test, predictions), 2),
            "training_samples": len(x_train),
            "test_samples": len(x_test),
            "categories": sorted(labels.unique().tolist()),
        }

    def predict_category(self, title, description):
        if not self.is_trained:
            self.train_and_evaluate()

        text = f"{title} {description}"
        prediction = self.model.predict([text])[0]
        probabilities = self.model.predict_proba([text])[0]
        confidence = max(probabilities)

        return {
            "category": str(prediction),
            "confidence": round(float(confidence), 2),
        }

    def _load_training_dataframe(self):
        return pd.read_csv(self.training_data_path)

    def _build_text_features(self, training_dataframe):
        return training_dataframe["title"] + " " + training_dataframe["description"]
