import joblib
import numpy as np

from flask import Flask
from flask import jsonify
from utils import Utils
from load_data import load_data

app = Flask(__name__)

X, y, countries, country_score = load_data('./in/happiness.csv')

@app.route('/predict', methods=['GET'])
def predict():    
    X_test = np.array([7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653])
    prediction = model.predict(X_test.reshape(1,-1))
    return jsonify({
        'actual_country_score':'7.537000179',
        'prediction': list(prediction)
    })

@app.route('/predict_all', methods=['GET'])
def predict_all():


    preds = model.predict(X).tolist()
    result = [
        {
            'country': country,
            'country_score': actual_country_score,
            'predicted_score': pred
        }
        for country, actual_country_score, pred in zip(countries, country_score, preds)
    ]

    return jsonify(result)


if __name__ == '__main__':
    utils = Utils()
    model = utils.load_model("./models/best_model.pkl")
    app.run(port=8080, debug=True)