def diagnose(report, raw):
    sorted_leaf_overall_color_contributions = sorted(report["leaf_overall_analysis_report"]["color_report"], key=lambda i: i['value'], reverse=True)
    return(sorted_leaf_overall_color_contributions)
