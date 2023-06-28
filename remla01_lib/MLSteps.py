
import re

import joblib
import nltk
import json
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class MLSteps:

    def __init__(self):        
        nltk.download("stopwords")

        self.ps = PorterStemmer()
        self.all_stopwords = stopwords.words("english")
        self.all_stopwords.remove("not")


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