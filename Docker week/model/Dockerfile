#base image
FROM python:3.8

#archivos necesarios
COPY fsa-headcount-as-at-31-january-2018.csv /app/
COPY model.py /app/

#creo directorio app en la imagen docker
WORKDIR /app

#instalo dependencias en la imagen
RUN pip install pandas numpy

#ejecuto comando para correr app en la imagen
CMD ["python", "model.py"]