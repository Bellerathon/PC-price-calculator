from difflib import SequenceMatcher
import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/CPU', methods=['POST'])
@cross_origin()
def search():
    data = request.get_json(force=True)
    target = data['query']
    print(target)
    similar_array = []
    f = open("/home/will/pcprice/backend/parts/cpus_array.txt", "r")
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
        if index == 10:
            break
        cpus.append(cpu["name"])

    return jsonify(cpus)
