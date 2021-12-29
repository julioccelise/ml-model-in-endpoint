from flask import Flask, jsonify, Response, request
from joblib import load

import sys
import traceback

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def predict():
    try:
        data = request.get_json()
        
        sepal_length = float(data['sepal_length'])
        sepal_width = float(data['sepal_width'])
        petal_length = float(data['petal_length'])
        petal_width = float(data['petal_width'])
        
        flower = [[sepal_length, sepal_width, petal_length, petal_width]]

        sc = load('predictor/standard_scaler.joblib')
        classifier = load('predictor/classifier.joblib')
        
        
        flower = sc.transform(flower)
        predicted_class = classifier.predict(flower)

        return jsonify({'class': predicted_class[0]})
    
    except:
        etype, value, tb = sys.exc_info()
        print(traceback.print_exception(etype, value, tb))
        return Response(status=500)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')