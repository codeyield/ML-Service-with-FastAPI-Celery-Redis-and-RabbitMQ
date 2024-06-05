from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Hey, what's up? What's new?",
            }
        }

class PredictionResult(BaseModel):
    label: str
    score: float
