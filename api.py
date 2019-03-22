from flask import Flask,jsonify,request
from queue import Queue

download_q = Queue()

app = Flask(__name__)

@app.route('/get/')
def home():
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

if __name__ == "__main__":
    app.run()
