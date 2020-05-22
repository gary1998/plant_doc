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
    url = request.args["url"]
    size = request.args["size"]
    mask_gray_low = request.args["mask_gray_low"]
    mask_gray_high = request.args["mask_gray_high"]
    health_point = request.args["health_point"]
    spot_area = request.args["spot_area"]
    raw = request.args["raw"]
    report = plant_doctor.generate_report(url=url, size=size, mask_gray_low=mask_gray_low, mask_gray_high=mask_gray_high, health_point=health_point, spot_area=spot_area, raw=raw)
    return jsonify(report=report)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=port)