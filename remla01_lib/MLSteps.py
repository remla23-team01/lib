
import re

import joblib
import nltk
import json
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class MLSteps:

    def __init__(self):
        # NLTK
        versionfile = json.load("version.json")
        current_version = versionfile['version']
        
        nltk.download("stopwords")

        self.ps = PorterStemmer()
        self.all_stopwords = stopwords.words("english")
        self.all_stopwords.remove("not")

        
        print("Initialized with version", current_version)
        self.current_version = current_version

    def get_model(self):
        """
        Load the model file.
        """
        return joblib.load("ml_models/c2_Classifier_Sentiment_Model")


    def get_count_vectorizer(self):
        """
        Load the CountVectorizer file.
        """
        return joblib.load("ml_models/c1_BoW_Sentiment_Model.pkl")


    def remove_stopwords(self, input: str) -> str:
        """
        Removes stopwords from the input string.

        Args:
            input (str): The string to remove stopwords from.

        Returns:
            str: The string without stopwords.
        """
        #   logger.debug("Removing stopwords...")
        review = re.sub("[^a-zA-Z]", " ", input)
        review = review.lower()
        review = review.split()
        review = [
            self.ps.stem(word) for word in review if not word in set(self.all_stopwords)
        ]
        result = " ".join(review)
        #   logger.debug("Stopwords removed.")
        return result



    def preprocess_review(self, review: str) -> np.ndarray:
        """
        Preprocesses the input review by removing stopwords and transforming it
        using the provided CountVectorizer.

        Args:
            review (str): The review to preprocess.

        Returns:
            np.ndarray: The preprocessed and transformed review.
        """
        review = self.remove_stopwords(review)
        cv = self.get_count_vectorizer()
        X = cv.transform([review]).toarray()
        return X

    def classify_review(self, review: str):
        """
        Makes a prediction based on the model and the input review.

        Args:
            review (str): The review to classify.

        Returns:
            int: The predicted sentiment label.
        """
        model = self.get_model()
        result = model.predict(review)
        return result