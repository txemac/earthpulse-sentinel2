from pydantic import BaseModel
from rasterio.coords import BoundingBox


class ImageAttributes(BaseModel):
    width: int
    height: int
    num_bands: int
    crs: str
    georeferenced: BoundingBox

    class Config:
        schema_extra = dict(
            example=dict(
                width=2186,
                height=1384,
                num_bands=12,
                crs="EPSG:4326",
                georeferenced=[-0.00839, 38.747216, 0.2381, 38.878028],
            )
        )
