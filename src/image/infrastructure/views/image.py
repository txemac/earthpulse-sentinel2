import rasterio
from fastapi import APIRouter
from fastapi import UploadFile
from starlette import status

from src.image.domain.image import ImageAttributes

images_router = APIRouter()


@images_router.post(
    path="/attributes",
    name="Get attributes",
    description="Receives the image as an input parameter and returns the following attributes: image size (width and "
                "height), number of bands, coordinate reference system and georeferenced bounding box.",
    status_code=status.HTTP_200_OK,
    response_model=ImageAttributes,
)
def get_attributes(
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
