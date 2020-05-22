def diagnose(report, raw, spot_count):
    sorted_leaf_overall_color_contributions = sorted(report["leaf_overall_analysis_report"]["color_report"], key=lambda i: i["value"], reverse=True)
    top_five_overall_colors = sorted_leaf_overall_color_contributions[0: 5]
    
    sorted_leaf_nerves_color_contributions = sorted(report["leaf_nerves_analysis_report"]["color_report"], key=lambda i: i["value"], reverse=True)
    top_five_nerves_colors = sorted_leaf_nerves_color_contributions[0: 5]

    yellow_overall_rank = next((index for (index, d) in enumerate(top_five_overall_colors) if d["name"] == "yellow"), None)
    purple_overall_rank = next((index for (index, d) in enumerate(top_five_overall_colors) if d["name"] == "purple"), None)
    red_overall_rank = next((index for (index, d) in enumerate(top_five_overall_colors) if d["name"] == "red"), None)
    yellow_green_overall_rank = next((index for (index, d) in enumerate(top_five_overall_colors) if d["name"] == "yellow_green"), None)
    
    yellow_nerve_rank = next((index for (index, d) in enumerate(top_five_nerves_colors) if d["name"] == "yellow"), None)

    yellow_spots = report["leaf_texture_analysis_report"]["yellow"]["presence"]
    brown_spots = report["leaf_texture_analysis_report"]["brown"]["presence"]
    red_spots = report["leaf_texture_analysis_report"]["red"]["presence"]

    yellow_spots_count = report["leaf_texture_analysis_report"]["yellow"]["count"]
    brown_spots_count = report["leaf_texture_analysis_report"]["brown"]["count"]
    red_spots_count = report["leaf_texture_analysis_report"]["red"]["count"]

    burning = bool(yellow_overall_rank in range(3,4))
    chlorosis = bool(yellow_overall_rank in range(1,2))
    interveinal_chlorosis = bool(yellow_nerve_rank in range(1,2))
    mottling = bool(yellow_spots or brown_spots or red_spots)
    necrosis = bool(brown_spots_count>=yellow_spots_count and brown_spots_count>=red_spots_count)
    phosphorous_deficiency = bool(purple_overall_rank or red_overall_rank)
    nitrogen_deficiency = bool((yellow_overall_rank or yellow_green_overall_rank) and not necrosis)
    molybdenum_deficiency = bool((yellow_overall_rank or yellow_green_overall_rank) and necrosis)
    magnesium_deficiency = bool(interveinal_chlorosis and red_spots_count>spot_count)
    potassium_deficiency = bool((not interveinal_chlorosis) and chlorosis and brown_spots_count>spot_count)
    chloride_deficiency = bool((not interveinal_chlorosis) and chlorosis and necrosis)
    raw_report = report if raw else None

    return {
        "burning": burning,
        "chlorosis": chlorosis,
        "interveinal_chlorosis": interveinal_chlorosis,
        "mottling": mottling,
        "necrosis": necrosis,
        "phosphorous_deficiency": phosphorous_deficiency,
        "nitrogen_deficiency": nitrogen_deficiency,
        "molybdenum_deficiency": molybdenum_deficiency,
        "magnesium_deficiency": magnesium_deficiency,
        "potassium_deficiency": potassium_deficiency,
        "chloride_deficiency": chloride_deficiency,
        "raw_report": raw_report
    }
