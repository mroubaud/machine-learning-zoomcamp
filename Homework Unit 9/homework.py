import numpy as np
#import tensorflow as tf
#cuando uso lambda sin tensorflow instalado en la docker image
import tflite_runtime.interpreter as tflite
#import tensorflow.lite as tflite
#import os

from keras_image_helper import create_preprocessor
from io import BytesIO
from urllib import request
from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    x /= 255
    return x

#name of the model
#MODEL_NAME = os.getenv('MODEL_NAME', 'tflite-bees-wasps.tflite')

#input size of the image in the model
target_size = (150,150)

#classes of the prediction
classes = ["bi"]

#preprocess the image for tlite
#preprocessor = create_preprocessor('xception', target_size=target_size)

#Load Tensorflow model and read it with tflite 
interpreter = tflite.Interpreter(model_path='bees-wasps-v2.tflite')
interpreter.allocate_tensors()

#input and output index for tflite model
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict (img_url = "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"):
  #prepare image
  #X = preprocessor.from_url(img_url)
  img = download_image(img_url)
  img_prepared = prepare_image(img, target_size)
  x = np.array(img_prepared, dtype="float32")
  X = np.array([x])
  X_preprocessed = preprocess_input(X)
  #print(X_preproc)
  interpreter.set_tensor(input_index, X_preprocessed)

  #get_predictions
  interpreter.invoke()
  preds = interpreter.get_tensor(output_index)
  float_predictions = preds[0].tolist()
  return dict(zip(classes, float_predictions))

def lambda_handler (event={"url": "https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg"}, context=""):
  url = event["url"]
  result = predict(url)
  print(result)
  return result

# predict()