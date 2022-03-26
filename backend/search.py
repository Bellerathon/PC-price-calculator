from difflib import SequenceMatcher
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
valid_parts = ["CPU", "GPU", "MOTHERBOARD", "RAM", "STORAGE", "FAN", "CASE", "POWERSUPPLY", "KEYBOARD", "MOUSE"]

@app.route('/searchPart', methods=['POST'])
@cross_origin()
def searchPart():
    data = request.get_json(force=True)
    part = secure_filename(data["part"])
    target = data["name"]
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

    return jsonify(cpus)

@app.route('/searchPartPrice', methods=['POST'])
@cross_origin()
def searchPartPrice():
    data = request.get_json(force=True)
    print(data["part"])
    return jsonify(data["part"])