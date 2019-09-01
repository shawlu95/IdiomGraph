import json

from flask import Flask
from flask import Flask, g, Response, request
app = Flask(__name__)

from py2neo import Graph
graph = Graph("bolt://localhost:7687", password="12345678")

def find_path(idiom, length, limit):
    cql = "match ()-[e:idiom {idiom: '%s'}]->()"%idiom
    path = "".join(["-[e%i:idiom]->()"%(i + 1) for i in range(length)])
    ret = ", ".join(["e%i.idiom as i%i"%(i + 1, i + 1) for i in range(length)])
    return graph.run(cql + path + " return e.idiom as i0, " + ret + " limit %i"%limit).to_data_frame()

@app.route("/")
def api_health_check():
    return "API online!"

@app.route("/find_next", methods=['GET'])
def find_next():
    idiom  = request.args.get('idiom', 'null')
    length  = int(request.args.get('length', 2))
    df_paths = find_path(idiom=idiom, length=length, limit=100000)
    return json.dumps(df_paths.to_dict(), indent=4, separators=(',', ':'))
