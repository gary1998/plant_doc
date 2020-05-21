from plantcv import plantcv as pcv
import json
import logging
from plant_doc.utils import color_reporter

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("health_calculator")

def calculate(rgb_img, mask):
    analysis_image = pcv.analyze_color(rgb_img, mask, 'hsv')
    logger.debug("image analyzed by PlantCV")
    all_colors = pcv.outputs.observations['hue_frequencies']['value']
    logger.debug('received all hue frequencies of the image')
    color_report = color_reporter.calculate_color_contribution(all_colors)
    logger.debug('received color report of the image')
    median_color = pcv.outputs.observations['hue_median']['value']
    logger.debug("median color of image calculated")
    logger.info(f'median color: {median_color}')
    health_score = round(1-(abs(median_color-120)/120), 2)
    logger.debug("health score of image calculated")
    logger.info(f'health score: {health_score}')
    return {
        "color_report": color_report,
        "dominant_color": median_color,
        "score": health_score
    }
