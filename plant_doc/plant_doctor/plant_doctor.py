import cv2
import numpy as np
from plantcv import plantcv as pcv
from plant_doc.utils import health_calculator, leaf_image, image_downloader, cache_remover, leaf_spots
from plant_doc.disease_estimator import disease_estimator


def generate_report(url, size=240, mask_gray_low=95, mask_gray_high=255, health_point=120, spot_area=50, raw=False):
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
    leaf_spots_report = leaf_spots.diagnose(rgb_img, mask, spot_area)

    cache_remover.clean()

    report = {
        "leaf_overall_analysis_report": leaf_health,
        "leaf_nerves_analysis_report": leaf_nerves_health,
        "leaf_branch_analysis_report": leaf_branch_health,
        "leaf_texture_analysis_report": leaf_spots_report
    }

    diagnosis = disease_estimator.diagnose(report, raw)

    return diagnosis
