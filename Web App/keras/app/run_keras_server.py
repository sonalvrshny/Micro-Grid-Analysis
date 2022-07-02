import os
import flask
from flask_cors import CORS
from pymongo import MongoClient
import time

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
CORS(app)
# initilize db
db_client = MongoClient('mongodb://db:27017/')
print(db_client.server_info())
mydb = db_client["enphase"]
mycol = mydb["data"]


def getOutput(hours, past, type):
    from keras.models import load_model
    from tensorflow import Graph, Session
    # import tensorflow as tf
    import numpy as np
    testData = np.array(past)
    testData = testData.reshape(1, len(past), 1)
    graph = Graph()
    with graph.as_default():
        session = Session()
        with session.as_default():
            # load model
            if(type == "load"):
                model = load_model("./model/model" + str(hours) + ".h5")
            elif(type == "generation"):
                model = load_model("./model/solar_model" + str(hours) + ".h5")
            model.summary()
            output = model.predict(testData)
            return output


@app.route("/predict", methods=["POST"])
def predict():
    if flask.request.method == "POST":
        req = flask.request.get_json()
        hours = req["hrs"]
        past = req["past"]
        type = req["type"]
        output = getOutput(hours, past, type)
        output = output.tolist()
    return flask.jsonify({"result": output})


@app.route("/solar_generation", methods=["POST"])
def display_generation():
    if flask.request.method == "POST":
        req = flask.request.get_json()
        type = req["type"]
        hours = req["hrs"]
        # GET data form db
        mydoc = mycol.find({}).sort('end_at',1)
        result = []
        to_pred = []
        past_power = []
        timestampepoch = []
        timestamp = []
        new_doc = []
        for i in range(0,mydoc.count(),3):
            new_doc.append(mydoc[i])
        for i in new_doc:
            del i["_id"]
            past_power.append(i["powr"])
            timestampepoch.append(i["end_at"])
            result.append(i)
        for i in range(12):
            timestampepoch.append(timestampepoch[len(timestampepoch)-1]+900)
        for i in timestampepoch:
            timestamp.append(time.strftime('%Y-%m-%d %H:%M:%S %Z',time.localtime(i+5*60*60+1800)))
        # new_res = []
        # for i in range(0,len(result),3):
        #     new_res.append(result[i])
        # for i in range(len(new_res)-24,len(new_res)):
        #     to_pred.append(new_res[i]["powr"])
        for i in range(len(result)-24,len(result)):
            to_pred.append(result[i]["powr"])
        output = getOutput(hours, to_pred, type)
        output = output.tolist()
        return flask.jsonify({"predicted": output,"past": past_power, "time_stamp": timestamp})


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
