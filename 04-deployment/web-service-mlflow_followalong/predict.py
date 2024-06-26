import pickle
import mlflow
from flask import Flask, request, jsonify


MLFLOW_TRACKING_URI = "http://127.0.0.1:5005/"
RUN_ID= 'bca046633ac94a0dacad64f65d5901fb'
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

logged_model = F'runs:/{RUN_ID}/models_pickle'
model = mlflow.pyfunc.load_model(logged_model)


def prepare_features(ride):
    features = {}
    features["PU_DO"] = "%s_%s" % (ride["PULocationID"], ride["DOLocationID"])
    features["trip_distance"] = ride["trip_distance"]
    return features


def predict(features):
    preds = model.predict(features)
    return preds[0]


app = Flask("duration-prediction-followalong")


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {"duration": pred, "model_version": RUN_ID}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9696)
