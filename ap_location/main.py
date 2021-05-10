import logging

import httpx
from fastapi import FastAPI

from .config import API_TOKEN, API_URL
from .models import ApScanData


logger = logging.getLogger(__name__)
app = FastAPI()

CACHE = {}


@app.post("/ap-location")
async def ap_location(ap_batch: ApScanData):
    logger.debug("Checking cache")
    if ap_batch.index in CACHE:
        logger.info("Found in cache")
        return CACHE[ap_batch.index]

    logger.info("Not found in cache")
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            API_URL,
            params={"key": API_TOKEN},
            json={"wifiAccessPoints": ap_batch.data},
        )
    CACHE[ap_batch.index] = resp.json()
    logger.debug("Stored result in cache")
    return resp.json()
