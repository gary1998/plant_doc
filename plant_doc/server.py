from flask import Flask, request, jsonify
from plant_doc.plant_doctor import plant_doctor
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def home():
    return "Welcome to PlantDoc"

@app.route("/analyze", methods=["GET"])
def analyze():
    args = request.args
    url = args.get("url", default=None)
    size = int(args.get("size", default=240))
    mask_gray_low = int(args.get("mask_gray_low", default=95))
    mask_gray_high = int(args.get("mask_gray_high", default=255))
    health_point = int(args.get("healh_point", default=120))
    spot_area = int(args.get("spot_area", default=50))
    spot_count = int(args.get("spot_count", default=100))
    raw = args.get("raw", default=False)
    report = plant_doctor.generate_report(url=url, size=size, mask_gray_low=mask_gray_low, mask_gray_high=mask_gray_high, health_point=health_point, spot_area=spot_area, spot_count=spot_count, raw=raw)
    return jsonify(report=report)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=port)