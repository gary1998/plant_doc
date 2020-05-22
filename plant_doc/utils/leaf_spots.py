import cv2
from plantcv import plantcv as pcv
import numpy as np
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("leaf_spots")

def diagnose(rbg_img, mask, spot_area):
    logger.debug("read rgb image, creating mask for it")
    img = cv2.bitwise_and(rbg_img, rbg_img, mask=mask)
    logger.debug("applied mask to rgb image")
    logger.debug("counting yellow spots")
    yellow_spots_count = count_yellow_spots(img, spot_area)
    logger.debug(f"got {yellow_spots_count} yellow spots")
    logger.debug("counting white spots")
    white_spots_count = count_white_spots(img, spot_area)
    logger.debug(f"got {white_spots_count} white spots")
    logger.debug("counting orange spots")
    orange_spots_count = count_orange_spots(img, spot_area)
    logger.debug(f"got {orange_spots_count} orange spots")
    return {
        "yellow": {
            "presence": bool(yellow_spots_count),
            "count": yellow_spots_count
        },
        "brown": {
            "presence": bool(white_spots_count),
            "count": white_spots_count
        },
        "red": {
            "presence": bool(orange_spots_count),
            "count": orange_spots_count
        }
    }

def count_yellow_spots(img, spot_area):
    masked_img = cv2.inRange(img, np.array([25, 100, 100]), np.array([35, 255, 255]))
    edges = pcv.canny_edge_detect(img=masked_img, sigma=0.1)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    spots = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cnt_area = w * h
        if cnt_area <= spot_area:
            spots.append(contour)
    return len(spots)

def count_brown_spots(img, spot_area):
    masked_img = cv2.inRange(img, np.array([16, 100, 100]), np.array([24, 255, 255]))
    edges = pcv.canny_edge_detect(img=masked_img, sigma=0.1)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    spots = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cnt_area = w * h
        if cnt_area <= spot_area:
            spots.append(contour)
    return len(spots)

def count_red_spots(img, spot_area):
    masked_img = cv2.inRange(img, np.array([175, 100, 100]), np.array([15, 255, 255]))
    edges = pcv.canny_edge_detect(img=masked_img, sigma=0.1)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    spots = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cnt_area = w * h
        if cnt_area <= spot_area:
            spots.append(contour)
    return len(spots)