import boto3
import joblib
import json
from flask import Flask, request ,jsonify

app = Flask(__name__)

s3 = boto3.resource('s3')
s3.meta.client.download_file('germancreditdata5', 'Modelo/modelrf.joblib', 'modelrf.joblib')

model = joblib.load("modelrf.joblib")

@app.route("/")
def index():
    return "Hi Flask"

@app.route("/predict",methods = ["POST"])
def predict():
    request_data = request.get_json()
    age = request_data["age"]
    credit_amount = request_data["credit_amount"]
    duration = request_data["duration"]
    sex = request_data["sex"]
    purpose = request_data["purpose"]
    housing = request_data["housing"]

    prediccion = model.predict([[age, credit_amount, duration, sex, purpose, housing]])

    diccionario = {"predict": prediccion.tolist()}

    salida = jsonify(diccionario)

    #return f"{age},{credit_amount},{purpose},{duration},{housing},{sex}"
    return salida

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
    #client = boto3.client("s3")
    #response = client.list_buckets()
    #for i in response['Buckets']:
    #    print(i['Name'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
