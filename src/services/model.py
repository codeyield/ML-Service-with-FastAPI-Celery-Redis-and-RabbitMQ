from loguru import logger
from transformers import pipeline
import torch

torch.set_num_threads(1)


class EmotionClassifier:
    """
    An emotion classifier based on a pre-trained Transformers model.

    Methods:
        predict_emotion: Predicting emotions from the text.
    """

    model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

    @classmethod
    def predict_emotion(cls, text: str):
        """
        Predicting emotions from the text.

        Args:
            text (str): A text for analysing emotions.

        Returns:
            dict: The result of the prediction as dictionary.
        """
        result = cls.model(text)[0]
        
        return result
