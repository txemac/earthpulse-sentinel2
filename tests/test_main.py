from starlette import status
from starlette.testclient import TestClient

from src.messages import API_TITLE
from src.messages import API_VERSION
from tests.utils import assert_dicts


def test_health(
        client: TestClient,
) -> None:
    response = client.get(
        url="/health",
    )
    assert response.status_code == status.HTTP_200_OK
    expected = dict(
        title=API_TITLE,
        status="OK",
        version=API_VERSION,
        time="*",
    )
    assert_dicts(original=response.json(), expected=expected)
