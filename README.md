# AP location

This is a FastAPI application that, including simple tests, and a Docker file
to ensure the environment is correctly setup. The setup uses Gunicorn as the
process manager and ASGI server (using uvicorn), with 2 cores set.

The current solution uses a simple in-process cache for it's simplicity. To
improve on this design, it is recommended using Redis and it's Hash table to store
the reply objects. This would allow the web server to go down and have the cache
persist.

The caching algorithm uses the RSSI and the BSSID to determine whether a signal
should be used to generate a hash. The RSSI threshold of `-82dBm` was chosen
because this is approximately the 10th percentile.

## Setup

You can build using the Dockerfile, or using a python venv, please note, this has
only been tested with python 3.7 and 3.9

### Docker setup

From this directory, please run:

```bash
docker build -t ap_location .
```

When this is complete, you have the docker environment setup.

### Using Python venv

In this directory, run:

```bash
python3 -m venv venv
```

Then:

```bash
./venv/bin/pip install -r requirements.txt
```

## Starting the webserver:

The webserver is an asynchronous web server, and has been setup to use Gunicorn
as the process manager. The Gunicorn setup at been set to use 2 cores, since this
allows for decent processor performance, and prevents too many cache misses.

It must be noted that caching is done per process - and not through a cache
server like redis. It would be recommended to use a separate caching database.

### Docker

To run the web server using Docker, run the following command. You will need to
provide the API_TOKEN as an environment variable:

```bash
docker run -e API_TOKEN <the api token> -it --rm -p 8001:8000 ap_location
```

This will now start the webserver and have it listening on port 8001

### Python venv

Note, you will need to pass the `API_TOKEN` in via an environment variable.

```bash
API_TOKEN=<api token> ./venv/bin/gunicorn ap_location.main:app -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001
```

This will start the web server listening on port 8001.

## Running the tests

Running the test is super easy!

### Running from Docker

```bash
docker run --rm ap_location pytest ap_location/test.py
```

### Running from Python venv

```bash
./venv/bin/pytest ap_location/test.py
```
