import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("color_reporter")

def calculate_color_contribution(hue_frequencies):
    return [
        {"name": "red", "value": calculate_red_contribution(hue_frequencies)},
        {"name": "red_orange", "value": calculate_red_orange_contribution(hue_frequencies)},
        {"name": "orange_brown", "value": calculate_orange_brown_contribution(hue_frequencies)},
        {"name": "orange_yellow", "value": calculate_orange_yellow_contribution(hue_frequencies)},
        {"name": "yellow", "value": calculate_yellow_contribution(hue_frequencies)},
        {"name": "yellow_green", "value": calculate_yellow_green_contribution(hue_frequencies)},
        {"name": "green", "value": calculate_green_contribution(hue_frequencies)},
        {"name": "green_cyan", "value": calculate_green_cyan_contribution(hue_frequencies)},
        {"name": "cyan", "value": calculate_cyan_contribution(hue_frequencies)},
        {"name": "cyan_blue", "value": calculate_cyan_blue_contribution(hue_frequencies)},
        {"name": "blue", "value": calculate_blue_contribution(hue_frequencies)},
        {"name": "blue_purple", "value": calculate_blue_purple_contribution(hue_frequencies)},
        {"name": "purple", "value": calculate_purple_contribution(hue_frequencies)},
        {"name": "purple_pink", "value": calculate_purple_pink_contribution(hue_frequencies)},
        {"name": "pink", "value": calculate_pink_contribution(hue_frequencies)},
        {"name": "pink_red", "value": calculate_pink_red_contribution(hue_frequencies)}
    ]

def calculate_red_contribution(hue_frequencies):
    contribution = 0
    for i in range(169, 179):
        contribution += hue_frequencies[i]
    for i in range(0, 5):
        contribution += hue_frequencies[i]
    return contribution

def calculate_red_orange_contribution(hue_frequencies):
    contribution = 0
    for i in range(6, 10):
        contribution += hue_frequencies[i]
    return contribution

def calculate_orange_brown_contribution(hue_frequencies):
    contribution = 0
    for i in range(11, 19):
        contribution += hue_frequencies[i]
    return contribution

def calculate_orange_yellow_contribution(hue_frequencies):
    contribution = 0
    for i in range(20, 24):
        contribution += hue_frequencies[i]
    return contribution

def calculate_yellow_contribution(hue_frequencies):
    contribution = 0
    for i in range(25, 31):
        contribution += hue_frequencies[i]
    return contribution

def calculate_yellow_green_contribution(hue_frequencies):
    contribution = 0
    for i in range(32, 39):
        contribution += hue_frequencies[i]
    return contribution

def calculate_green_contribution(hue_frequencies):
    contribution = 0
    for i in range(40, 66):
        contribution += hue_frequencies[i]
    return contribution

def calculate_green_cyan_contribution(hue_frequencies):
    contribution = 0
    for i in range(67, 84):
        contribution += hue_frequencies[i]
    return contribution

def calculate_cyan_contribution(hue_frequencies):
    contribution = 0
    for i in range(85, 99):
        contribution += hue_frequencies[i]
    return contribution

def calculate_cyan_blue_contribution(hue_frequencies):
    contribution = 0
    for i in range(100, 109):
        contribution += hue_frequencies[i]
    return contribution

def calculate_blue_contribution(hue_frequencies):
    contribution = 0
    for i in range(110, 120):
        contribution += hue_frequencies[i]
    return contribution

def calculate_blue_purple_contribution(hue_frequencies):
    contribution = 0
    for i in range(121, 139):
        contribution += hue_frequencies[i]
    return contribution

def calculate_purple_contribution(hue_frequencies):
    contribution = 0
    for i in range(140, 159):
        contribution += hue_frequencies[i]
    return contribution

def calculate_purple_pink_contribution(hue_frequencies):
    contribution = 0
    for i in range(160, 164):
        contribution += hue_frequencies[i]
    return contribution

def calculate_pink_contribution(hue_frequencies):
    contribution = 0
    for i in range(165, 172):
        contribution += hue_frequencies[i]
    return contribution

def calculate_pink_red_contribution(hue_frequencies):
    contribution = 0
    for i in range(173, 176):
        contribution += hue_frequencies[i]
    return contribution