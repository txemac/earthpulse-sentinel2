from src.image.application.get_thumbnail import get_thumbnail


def test_get_thumbnail_ok(
        file_tiff: bytes,
) -> None:
    assert get_thumbnail(file=file_tiff) is not None
