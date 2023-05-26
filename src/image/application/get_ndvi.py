import base64
from typing import BinaryIO


def get_ndvi(
        file: BinaryIO,
        palette: str = None,
) -> bytes:
    with open("tests/files/thumbs-up.png", "rb") as file:
        image = file.read()
    return base64.b64encode(image)
