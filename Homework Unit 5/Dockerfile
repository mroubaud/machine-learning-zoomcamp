#create image of the model made in python
FROM svizor/zoomcamp-model:3.10.12-slim

#install pipenv in python image
RUN pip install pipenv

#working directory: where the image will be
WORKDIR /app

#copio versiones de librerías utilizadas en la imagen
#lo copio con la info que hay en Pipfile y Piffile.lock 
#"./" es para referenciar desde donde, from current dir
COPY ["Pipfile", "Pipfile.lock", "./"]

#install all libraries en el virtual envierment
RUN pipenv install --system --deploy

#Copio el programa predict_prac que tenía creado para predecir
COPY ["predict_q6.py", "./"]


#expongo puerto 9696 para consultas por ese puerto a la app
EXPOSE 9696

#Run gunicorn and listen on local host 0:0:0:0 port 9696
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict_q6:app"]