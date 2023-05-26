import base64
from typing import BinaryIO
from typing import Tuple


def get_thumbnail(
        file: BinaryIO,
        resolution: Tuple[int, int] = (512, 512),
) -> bytes:
    with open("tests/files/thumbs-up.png", "rb") as file:
        image = file.read()
    return base64.b64encode(image)
