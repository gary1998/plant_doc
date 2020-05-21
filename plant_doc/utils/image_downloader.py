import logging
import sys
import requests
import os

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("image_downloader")

def download_and_save(url):
    logger.debug(f"making request to server with url: {url}")
    resp = requests.get(url=url, verify=False)
    logger.debug("response received from server")
    file_path = "./plant_doc/test_images/test"+str(url[url.rindex("."): len(url)])
    logger.debug("creating file to write response content")
    with open(file_path, "wb+") as f:
        logger.debug("file created")
        f.write(resp.content)
        logger.debug("file written")
    return file_path