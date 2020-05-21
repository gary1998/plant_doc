import cv2
from plantcv import plantcv as pcv
import logging
import json

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("leaf_image")

def prepare(rgb_img):
    logger.debug('received rbg image')
    gray_img = pcv.rgb2gray(rgb_img=rgb_img)
    logger.debug('converted rbg image to grayscale image')
    masked_img = cv2.inRange(gray_img, 95, 255)
    logger.debug('filtered grayscale image')
    fill_image = pcv.fill_holes(masked_img)
    logger.debug('filled holes in binary mask')
    logger.debug('returned binary image mask')
    return fill_image
