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
    report = plant_doctor.generate_report(url)
    return jsonify(report=report)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=port)