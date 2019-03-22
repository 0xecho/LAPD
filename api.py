from flask import Flask,jsonify,request
from queue import Queue

download_q = Queue()

app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({"TO_THE_GUEST":"WELCOME TO THE LAPD ;-)"})

@app.route('/get/')
def get():
    if not download_q.empty():
        return jsonify({"success":True,"url":download_q.get()})
    return jsonify({"success":False,"error":"Queue empty"})

@app.route('/add/')
def add():
    url=request.args.get("url","")
    try:
        download_q.put(url)
        return jsonify({"success":True,"url":url})
    except:
        pass
    return jsonify({"success":False,"error":"cant add to the queue"})
