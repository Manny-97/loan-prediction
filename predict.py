import pickle

from flask import Flask, request, jsonify

with open('models/model.bin', 'rb') as f_in:
    (model) = pickle.load(f_in)



def predict(features):
    pred = model.predict(features)
    return int(pred)


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    features = request.get_json()

    pred = predict(features)

    result = {
        'loan_status': pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)