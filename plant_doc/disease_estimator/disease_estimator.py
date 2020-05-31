import datetime

def diagnose(report, raw, spot_count):
    sorted_leaf_overall_color_contributions = sorted(
        report["leaf_overall_analysis_report"]["color_report"], key=lambda i: i["value"], reverse=True)
    top_five_overall_colors = sorted_leaf_overall_color_contributions[0: 5]

    sorted_leaf_nerves_color_contributions = sorted(
        report["leaf_nerves_analysis_report"]["color_report"], key=lambda i: i["value"], reverse=True)
    top_five_nerves_colors = sorted_leaf_nerves_color_contributions[0: 5]

    yellow_overall_rank = next((index for (index, d) in enumerate(
        top_five_overall_colors) if d["name"] == "yellow"), None)
    purple_overall_rank = next((index for (index, d) in enumerate(
        top_five_overall_colors) if d["name"] == "purple"), None)
    red_overall_rank = next((index for (index, d) in enumerate(
        top_five_overall_colors) if d["name"] == "red"), None)
    yellow_green_overall_rank = next((index for (index, d) in enumerate(
        top_five_overall_colors) if d["name"] == "yellow_green"), None)

    yellow_nerve_rank = next((index for (index, d) in enumerate(
        top_five_nerves_colors) if d["name"] == "yellow"), None)

    yellow_spots = report["leaf_texture_analysis_report"]["yellow"]["presence"]
    brown_spots = report["leaf_texture_analysis_report"]["brown"]["presence"]
    red_spots = report["leaf_texture_analysis_report"]["red"]["presence"]

    yellow_spots_count = report["leaf_texture_analysis_report"]["yellow"]["count"]
    brown_spots_count = report["leaf_texture_analysis_report"]["brown"]["count"]
    red_spots_count = report["leaf_texture_analysis_report"]["red"]["count"]

    burning = bool(yellow_overall_rank in range(3, 4))
    chlorosis = bool(yellow_overall_rank in range(1, 2))
    interveinal_chlorosis = bool(yellow_nerve_rank in range(1, 2))
    mottling = bool(yellow_spots or brown_spots or red_spots)
    necrosis = bool(brown_spots_count >=
                    yellow_spots_count and brown_spots_count >= red_spots_count)
    phosphorous_deficiency = bool(purple_overall_rank or red_overall_rank)
    nitrogen_deficiency = bool(
        (yellow_overall_rank or yellow_green_overall_rank) and not necrosis)
    molybdenum_deficiency = bool(
        (yellow_overall_rank or yellow_green_overall_rank) and necrosis)
    magnesium_deficiency = bool(
        interveinal_chlorosis and red_spots_count > spot_count)
    potassium_deficiency = bool(
        (not interveinal_chlorosis) and chlorosis and brown_spots_count > spot_count)
    chloride_deficiency = bool(
        (not interveinal_chlorosis) and chlorosis and necrosis)

    diagnosed_report = {
        "dt": datetime.datetime.now().timestamp()*1000
        "diseases": [],
        "deficiencies": [],
    }

    if chlorosis:
        diagnosed_report["diseases"].append({
            "name": "chlorosis",
            "text": "Chlorosis is generally caused due to lack of Iron in plants. Use some Iron based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if burning:
        diagnosed_report["diseases"].append({
            "name": "burning",
            "text": "Burning is caused due to scorching sun light. Keep plants in shade for the time sun light is highest in day."
        })
    if interveinal_chlorosis:
        diagnosed_report["diseases"].append({
            "name": "interveinal_chlorosis",
            "text": "Interveinal Chlorosis is generally caused due to lack of Iron or Magnesium in plants. Use some Iron and Magnesium based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if mottling:
        diagnosed_report["diseases"].append({
            "name": "mottling",
            "text": "Mottling in leaves can be sign of bacterial or fungal infection on smaller portion of crop or disease on whole crop. If Mottling is seen on almost all leaves, use Calcium and Magnesium based fertilizer or use some fungicide to spray over bacteria or fungus infected portions of crop. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if necrosis:
        diagnosed_report["diseases"].append({
            "name": "necrosis",
            "text": "Necrosis in leaves can be sign of bacterial or fungal infection on smaller portion of crop or disease on whole crop. If Mottling is seen on almost all leaves, use Phosphorous based fertilizer or use some fungicide to spray over bacteria or fungus infected portions of crop. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if phosphorous_deficiency:
        diagnosed_report["deficiencies"].append({
            "name": "phosphorous_deficiency",
            "text": "Use Phosphorous based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if nitrogen_deficiency:
        diagnosed_report["deficiencies"].append({
            "name": "nitrogen_deficiency",
            "text": "Use Nitrogen based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if molybdenum_deficiency:
        diagnosed_report["deficiencies"].append({
            "name": "molybdenum_deficiency",
            "text": "Use Molybdenum based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if magnesium_deficiency:
        diagnosed_report["deficiencies"].append({
            "name": "magnesium_deficiency",
            "text": "Use Magnesium based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if potassium_deficiency:
        diagnosed_report["deficiencies"].append({
            "name": "potassium_deficiency",
            "text": "Use Potassium based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if chloride_deficiency:
        diagnosed_report["deficiencies"].append({
            "name": chloride_deficiency,
            "text": "Use Chloride based fertilizer. Fertilizer's amount should be fixed according to field area and yield amount."
        })
    if raw:
        diagnosed_report["raw"] = report

    return diagnosed_report
