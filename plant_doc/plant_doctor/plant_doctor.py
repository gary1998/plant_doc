import cv2
import numpy as np
from plantcv import plantcv as pcv
from plant_doc.utils import health_calculator, leaf_image, image_downloader, cache_remover
from plant_doc.disease_diagnosers import leaf_spots


def generate_report(url):
    path = image_downloader.download_and_save(url)
    rgb_img = cv2.imread(path)
    rgb_img = cv2.resize(rgb_img, (240, 240))
    mask = leaf_image.prepare(rgb_img)

    # Leaf Health Analysis Report
    leaf_health = health_calculator.calculate(rgb_img, mask)
    skeleton = pcv.morphology.skeletonize(mask=mask)

    # Leaf Nerves Health Analysis Report
    leaf_nerves_health = health_calculator.calculate(rgb_img, skeleton)
    leaf_branch_points_img = pcv.morphology.find_branch_pts(skel_img=skeleton, mask=mask)

    # Leaf Branches Health Analysis Report
    leaf_branch_health = health_calculator.calculate(rgb_img, leaf_branch_points_img)

    # Leaf Spots Analysis Report
    leaf_spots_report = leaf_spots.diagnose(rgb_img, mask)

    cache_remover.clean()

    return {
        "leaf_overall_analysis_report": leaf_health,
        "leaf_nerves_analysis_report": leaf_nerves_health,
        "leaf_branch_analysis_report": leaf_branch_health,
        "leaf_texture_analysis_report": leaf_spots_report
    }
