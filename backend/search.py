from difflib import SequenceMatcher
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
valid_parts = ["CPU", "GPU", "MOTHERBOARD", "RAM", "STORAGE", "FAN", "CASE", "POWERSUPPLY", "KEYBOARD", "MOUSE", "MONITOR", "COOLER"]

@app.route('/searchPart', methods=['POST'])
@cross_origin()
def searchPart():
    data = request.get_json(force=True)
    part = secure_filename(data["part"])
    target = data["name"]
    print(target)
    if part not in valid_parts:
        return jsonify("Invalid part")
    f = open(f"/home/will/pcprice/backend/parts/{part}.txt", "r")
    similar_array = []
    for line in f:
        cpu = {}
        line = line.strip("\n")
        if SequenceMatcher(None, target, line).ratio() == 1.0:
            return jsonify(line)
        else:
            cpu["name"] = line
            current_similarity = SequenceMatcher(None, target, line).ratio()
            cpu["similarity"] = current_similarity
            similar_array.append(cpu)

    f.close()

    newlist = sorted(similar_array, key=lambda d: d["similarity"])
    newlist = reversed(newlist)
    cpus = []
    for index, cpu in enumerate(newlist):
        if index == 15:
            break
        cpus.append(cpu["name"])
    print(cpus)
    return jsonify(cpus)

@app.route('/searchPartPrice', methods=['POST'])
@cross_origin()
def searchPartPrice():
    data = request.get_json(force=True)
    print(data["part"])
    prices = [460.00,   386.00,   370.00,   450.00,   500.00,   331.00,   414.42, 426.41, 373.11, 474.32,
    439.74, 426.41, 491.91, 413.09, 360.15, 395.28, 466.39, 456.77, 549.67, 527.04,
    356.63]
    return jsonify(prices)