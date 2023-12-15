FROM python:3.10-alpine

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY ./requirements.text .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
