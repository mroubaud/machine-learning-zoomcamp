import pandas as pd
import numpy as np
import pickle
from flask import Flask
from flask import request
from flask import jsonify

dv_input_file = 'dv.bin'
model_input_file = 'model2.bin'

with open(dv_input_file, 'rb') as dv_input_file:
  dv=pickle.load(dv_input_file)

with open(model_input_file, 'rb') as model_input_file:
  model=pickle.load(model_input_file)
app = Flask("score")

@app.route("/predict", methods=["POST"])
def predict():
  customer = request.get_json()
  X = dv.transform(customer)
  y_pred = model.predict_proba(X)[0,1]
  score = (y_pred >0.5)
  result = {
    "score_prob": float(y_pred),
    "score": bool(score)
  }
  return jsonify(result)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=9696)