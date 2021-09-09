FROM python:3.10.0rc2-alpine3.14

ENV SERVICE="Serviço A"

WORKDIR /app

COPY python-backend.zip .

RUN unzip python-backend.zip && pip3 install -r requirements.txt

CMD ["python", "app.py"]
