import cv2
import numpy as np
from plantcv import plantcv as pcv
from plant_doc.utils import health_calculator, leaf_image, image_downloader, cache_remover, leaf_spots
from plant_doc.disease_estimator import disease_estimator
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("plant_doctor")

def generate_report(url, size, mask_gray_low, mask_gray_high, health_point, spot_area, spot_count, raw):
    logger.debug("got path arguments as followed:")
    logger.debug(f"url = {url}")
    logger.debug(f"mask_gray_low = {mask_gray_low}")
    logger.debug(f"mask_gray_high = {mask_gray_high}")
    logger.debug(f"health_point = {health_point}")
    logger.debug(f"spot_area = {spot_area}")
    logger.debug(f"spot_count = {spot_count}")
    logger.debug(f"raw = {raw}")
    if(url):
        path = image_downloader.download_and_save(url)
        rgb_img = cv2.imread(path)
        rgb_img = cv2.resize(rgb_img, (size, size))
        mask = leaf_image.prepare(rgb_img, mask_gray_low, mask_gray_high)

        # Leaf Health Analysis Report
        leaf_health = health_calculator.calculate(rgb_img, mask, health_point)
        skeleton = pcv.morphology.skeletonize(mask=mask)

        # Leaf Nerves Health Analysis Report
        leaf_nerves_health = health_calculator.calculate(rgb_img, skeleton, health_point)
        leaf_branch_points_img = pcv.morphology.find_branch_pts(skel_img=skeleton, mask=mask)

        # Leaf Branches Health Analysis Report
        leaf_branch_health = health_calculator.calculate(rgb_img, leaf_branch_points_img, health_point)

        # Leaf Spots Analysis Report
        leaf_spots_report = leaf_spots.diagnose(rgb_img, mask, spot_area, spot_count)

        cache_remover.clean()

        report = {
            "leaf_overall_analysis_report": leaf_health,
            "leaf_nerves_analysis_report": leaf_nerves_health,
            "leaf_branch_analysis_report": leaf_branch_health,
            "leaf_texture_analysis_report": leaf_spots_report
        }

        diagnosis = disease_estimator.diagnose(report, raw, spot_count)

        return diagnosis

    else:
        return "url path argument is required"
