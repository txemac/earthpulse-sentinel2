# EarthPulse Backend Coding Challenge

The objective of this test is to evaluate the candidate’s ability developing Python backends and web applications with
geospatial data. You are asked to build a Python web API to work with the provided Sentinel 2 satellite image and
fulfill the following requirements:

1. An `/attributes` endpoint that receives the image as an input parameter, reads the image and returns the
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

# Solution

Considerations:

- the first consideration is to use FastAPI as web framework to create the API, it is fast and with a big community
  behind.
- Documentation, other big point of FastAPI... easy and automatic.
- Continuous integration with GitHub action, necessary to check tests and the linting with flake8.
- All endpoints are to get info... so the normal way is to use GET endpoints. In this system the endpoints need to
  receive an image like input parameter. The definition of GET requests don't have the option to send a file, so,
  one solution is to use POST endpoints and send the file like a parameter.

## Run

### Terminal with virtual env

If you want to run the app in a terminal, the first step is to install dependencies:

```shell script
pip install -r src/requirements.txt
pip install -r tests/requirements.txt
```

Run the API:

```shell script
uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```

Test:

```shell script
pytest -vvv
```

### Docker

Run the API:

```shell script
docker-compose up -d --build
```

Stop:

```shell script
docker-compose stop
```

Check the API with http://127.0.0.1:8000/health

## Documentation

http://127.0.0.1:8000/redoc

or swagger in:

http://127.0.0.1:8000/docs
