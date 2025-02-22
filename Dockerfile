#make this code as image then deployment
FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app   
#create app directory and copy all the code
COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]