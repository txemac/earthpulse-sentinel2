from typing import Tuple

import rasterio
from fastapi import APIRouter
from fastapi import UploadFile
from starlette import status

from src.image.application.get_thumbnail import get_thumbnail
from src.image.domain.image import ImageAttributes
from src.image.domain.image import ImageBase64

images_router = APIRouter()


@images_router.post(
    path="/attributes",
    name="Get attributes",
    description="Receives the image as an input parameter and returns the following attributes: image size (width and "
                "height), number of bands, coordinate reference system and georeferenced bounding box.",
    status_code=status.HTTP_200_OK,
    response_model=ImageAttributes,
)
def post_attributes(
        file: UploadFile,
) -> ImageAttributes:
    with rasterio.open(file.file) as dataset:
        result = ImageAttributes(
            width=dataset.width,
            height=dataset.height,
            num_bands=dataset.count,
            crs=str(dataset.crs),
            georeferenced=dataset.bounds,
        )

    return result


@images_router.post(
    path="/thumbnail",
    name="Get thumbnail",
    description="Returns an RGB thumbnail of the image as a PNG.",
    status_code=status.HTTP_200_OK,
    response_model=ImageBase64,
)
def post_thumbnail(
        file: UploadFile,
        resolution: Tuple[int, int] = (512, 512),
) -> ImageBase64:
    image: bytes = get_thumbnail(file=file.file, resolution=resolution)
    return ImageBase64(image=image)
