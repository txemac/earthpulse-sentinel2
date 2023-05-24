# EarthPulse Backend Coding Challenge

The objective of this test is to evaluate the candidate’s ability developing Python backends and web applications with
geospatial data. You are asked to build a Python web API to work with the provided Sentinel 2 satellite image and
fulfill the following requirements:

1. An `/attributes endpoint that receives the image as an input parameter, reads the image and returns the
   following [attributes](https://rasterio.readthedocs.io/en/latest/quickstart.html#dataset-attributes) as a JSON
   object: image size (width and height), number of bands, coordinate reference system and georeferenced bounding box.
2. A `/thumbnail` endpoint that receives the image as an input parameter and returns an RGB thumbnail of the image as a
   PNG. Consider accepting also the target resolution of the thumbnail as an additional optional parameter.
3. An `/ndvi` endpoint that receives the image, computes
   an [NDVI](https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index) on the image and returns the result
   as a colored PNG. Consider accepting the
   target [palette](https://matplotlib.org/stable/tutorials/colors/colormaps.html) for coloring the NDVI as an
   additional optional input.

You can download the satellite image
from [here](https://drive.google.com/file/d/1lDnU3UtBsdJ7KEEgao6hQmgC-Yr140l8/view?usp=sharing). You are encouraged to
use the following libraries:

1. [FastAPI](https://fastapi.tiangolo.com) as a Python API framework.
2. [Rasterio](https://rasterio.readthedocs.io/en/latest/) for working with the satellite image.
3. [NumPy](https://numpy.org), [Matplotlib](https://matplotlib.org) and [PIL](https://pillow.readthedocs.io/en/stable/)
   for handling the data and visualizations.

The test is designed to be completed in 2-3 of hours at maximum with about 50 lines of code (ignoring comments and line
breaks). Past this time, provide a link to a Github repository with your solution (if the repository is private, make
sure to share it with us). The repository should contain a README file with instructions on how to run the application
and a small documentation of the three endpoints with examples of inputs and outputs. For extra points, consider adding
testing and Docker support to the application.

Be creative and don’t hesitate to show off your skills!

If you have any doubt, send an email to careers@earthpulse.es.
