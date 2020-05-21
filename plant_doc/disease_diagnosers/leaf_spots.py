import cv2
from plantcv import plantcv as pcv
import numpy as np
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("leaf_spots")

def diagnose(rbg_img, mask):
    logger.debug("read rgb image, creating mask for it")
    img = cv2.bitwise_and(rbg_img, rbg_img, mask=mask)
    logger.debug("applied mask to rgb image")
    logger.debug("counting yellow spots")
    yellow_spots_count = count_yellow_spots(img)
    logger.debug(f"got {yellow_spots_count} yellow spots")
    logger.debug("counting white spots")
    white_spots_count = count_white_spots(img)
    logger.debug(f"got {white_spots_count} white spots")
    logger.debug("counting orange spots")
    orange_spots_count = count_orange_spots(img)
    logger.debug(f"got {orange_spots_count} orange spots")
    return {
        "yellow": {
            "presence": bool(yellow_spots_count),
            "count": yellow_spots_count
        },
        "white": {
            "presence": bool(white_spots_count),
            "count": white_spots_count
        },
        "orange": {
            "presence": bool(orange_spots_count),
            "count": orange_spots_count
        }
    }

def count_yellow_spots(img):
    masked_img = cv2.inRange(img, np.array([21, 100, 100]), np.array([32, 255, 255]))
    edges = pcv.canny_edge_detect(img=masked_img, sigma=0.1)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    spots = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cnt_area = w * h
        if cnt_area <= 50:
            spots.append(contour)
    return len(spots)

def count_white_spots(img):
    masked_img = cv2.inRange(img, np.array([0, 10, 153]), np.array([180, 25, 255]))
    edges = pcv.canny_edge_detect(img=masked_img, sigma=0.1)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    spots = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cnt_area = w * h
        if cnt_area <= 50:
            spots.append(contour)
    return len(spots)

def count_orange_spots(img):
    masked_img = cv2.inRange(img, np.array([7, 100, 100]), np.array([20, 255, 255]))
    edges = pcv.canny_edge_detect(img=masked_img, sigma=0.1)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    spots = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cnt_area = w * h
        if cnt_area <= 50:
            spots.append(contour)
    return len(spots)