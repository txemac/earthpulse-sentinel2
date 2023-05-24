import os
from datetime import datetime
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

from src.messages import API_TITLE
from src.messages import API_VERSION

os.environ["TZ"] = "UTC"

# create the api
api = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
)


# health endpoint
class HealthOut(BaseModel):
    title: str
    status: str
    version: str
    time: datetime

    class Config:
        schema_extra = dict(
            example=dict(
                title=API_TITLE,
                status="OK",
                version=API_VERSION,
                time=datetime.utcnow(),
            )
        )


@api.get(
    path="/health",
    tags=["Health"],
    description="Check the health of the API.",
    status_code=status.HTTP_200_OK,
    response_model=HealthOut,
)
def health() -> Dict:
    return dict(
        title=API_TITLE,
        status="OK",
        version=API_VERSION,
        time=datetime.utcnow(),
    )
