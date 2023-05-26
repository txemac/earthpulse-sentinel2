from src.image.application.get_ndvi import get_ndvi


def test_get_ndvi_ok(
        file_tiff: bytes,
) -> None:
    assert get_ndvi(file=file_tiff) is not None
