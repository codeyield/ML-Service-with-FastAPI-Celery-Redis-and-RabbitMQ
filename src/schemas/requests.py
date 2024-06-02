from pydantic import BaseModel


class TextRequest(BaseModel):
    """
    A query model for emotion classification from text.

    Attributes:
        text (str): A text for analysing emotions.
    """

    text: str

    class Config:
        """Model example."""

        schema_extra = {
            "example": {
                "text": "Hey, what's up? What's new?",
            }
        }
