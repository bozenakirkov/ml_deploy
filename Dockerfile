FROM continuumio/anaconda3
COPY /ml_deploy /usr/local/ml_deploy
EXPOSE 5000
WORKDIR /usr/local/ml_deploy/
RUN pip install -r requirements.txt
CMD python ./app.py