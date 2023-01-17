import pickle
import pandas as pd
from flask import Flask, request, jsonify

with open('models/model.bin', 'rb') as f_in:
    (model) = pickle.load(f_in)

def loan_status(value: int) -> str:
    status = {1:'Yes', 0:'No'}
    return status[value]

def predict(features):
    pred = model.predict(features)
    return int(pred)


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    features = request.get_json()
    features = pd.DataFrame({'column1': [features]}, index=[0])
    features = pd.DataFrame(features['column1'].values.tolist(), index=features.index)
    pred = predict(features)

    result = {
        'loan_status': loan_status(pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)