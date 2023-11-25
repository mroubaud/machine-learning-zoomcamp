#importo imagen con el modelo en formato tflite, la imagen fue descargada previamente
FROM agrigorev/zoomcamp-bees-wasps:v2
# instalo libreria keras-image-helper para preprocesar imagen
RUN pip install keras-image-helper
#instalo tflite para aws lambda
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

#ENV MODEL_NAME = bees-wasps-v2.tflite

#copio programa homework que preprocesa la imagen y tiene lambda handler
COPY homework.py .
#ejecuto lambda_handler dentro de archivo homework
CMD ["homework.lambda_handler"]