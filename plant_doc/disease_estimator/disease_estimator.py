def diagnose(report, raw):
    if(raw):
        return report
    else:
        return {
            "msg": "not raw"
        }