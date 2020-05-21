import os
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("cache_remover")

def clean():
    logger.debug("clearing test_images")
    directory = "./plant_doc/test_images"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".tiff") or file.endswith(".gif"))]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)
    logger.debug("cleaned test_images")
