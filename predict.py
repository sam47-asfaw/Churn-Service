from flask import Flask, jsonify, request
from waitress import serve

import pickle

with open('./model_C=1.0.bin', 'rb') as f_in:
    (dv, model)= pickle.load(f_in)

app = Flask('churn')

#transform the 
def transform(customer):
    return dv.transform(customer)



@app.route('/predict', methods= ['POST'])
def predict():
    customer = request.get_json()
    X = transform(customer)
    prediction = float(model.predict_proba(X))
    churn = bool(prediction < 0.5)

    
    result = {
        'Churn Probablility': prediction,
        'churn': churn,
        'Customer Status': ''
    }

    if churn < 0.5:
        result['Customer Status'] = 'Customer is likely to churn, send promotional email.'
        return jsonify(result)
    elif churn >= 0.5 and churn < 1.5:
        result['Customer Status'] = 'Welcome to our telecom service.'
        return jsonify(result)
    else:
        result['Customer Status'] = 'Thank you for being valued customer'
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)


