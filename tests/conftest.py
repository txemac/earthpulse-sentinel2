from io import IOBase
from typing import Any
from typing import Generator

import pytest
from starlette.config import environ
from starlette.testclient import TestClient

from src.main import api

environ["TESTING"] = "True"


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    with TestClient(api) as client:
        yield client


@pytest.fixture
def file_tiff() -> IOBase:
    with open("tests/files/S2L2A_2022-06-09.tiff", "rb") as file:
        result = file.read()
    return result
