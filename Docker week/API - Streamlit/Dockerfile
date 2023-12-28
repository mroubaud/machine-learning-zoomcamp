#install python imae
FROM python:3.9-slim

#creo y voy a diredctorio de trabajo en la imagen
WORKDIR /app

#instalo git en la imagen
COPY ["main.py", "requirements.txt", "./"]

#instalo requerimientos de la app de streamlit
RUN pip install -r requirements.txt

#expongo puerto 8501 que es el que usa streamlit, escucho ese puerto
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#ejecuto comandos para correr la app en 
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
