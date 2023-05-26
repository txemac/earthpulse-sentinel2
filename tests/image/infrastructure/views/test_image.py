from starlette import status
from starlette.testclient import TestClient

from tests.utils import assert_dicts


def test_post_attributes_ok(
        client: TestClient,
) -> None:
    response = client.post(
        url="/images/attributes",
        files=dict(file=open("tests/files/S2L2A_2022-06-09.tiff", "rb")),
    )
    assert response.status_code == status.HTTP_200_OK
    expected = {
        "width": 2186,
        "height": 1384,
        "num_bands": 12,
        "crs": "EPSG:4326",
        "georeferenced": [-0.00839, 38.747216, 0.2381, 38.878028]
    }
    assert_dicts(original=response.json(), expected=expected)


def test_post_attributes_no_file(
        client: TestClient,
) -> None:
    response = client.post(
        url="/images/attributes",
        files=None,
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"


def test_post_thumbnail_ok(
        client: TestClient,
) -> None:
    response = client.post(
        url="/images/thumbnail",
        files=dict(file=open("tests/files/S2L2A_2022-06-09.tiff", "rb")),
    )
    assert response.status_code == status.HTTP_200_OK


def test_post_thumbnail_no_file(
        client: TestClient,
) -> None:
    response = client.post(
        url="/images/thumbnail",
        files=None,
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"
