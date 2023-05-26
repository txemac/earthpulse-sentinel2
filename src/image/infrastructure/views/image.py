import rasterio
from fastapi import APIRouter
from fastapi import UploadFile
from starlette import status

from src.image.application.get_ndvi import get_ndvi
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
) -> ImageBase64:
    image: bytes = get_thumbnail(file=file.file, resolution=(512, 512))
    return ImageBase64(image=image)


@images_router.post(
    path="/ndvi",
    name="Get ndvi",
    description="Computes an NDVI on the image and returns the result as a colored PNG.",
    status_code=status.HTTP_200_OK,
    response_model=ImageBase64,
)
def post_ndvi(
        file: UploadFile,
) -> ImageBase64:
    image: bytes = get_ndvi(file=file.file, palette="palette")
    return ImageBase64(image=image)
