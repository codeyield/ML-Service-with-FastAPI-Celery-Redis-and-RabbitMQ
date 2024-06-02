from pydantic import BaseModel


class HealthcheckResult(BaseModel):
    """
    A query model for healthchecking

    Args:
        BaseModel (_type_): _description_
    """
    is_alive: bool
    date: str
