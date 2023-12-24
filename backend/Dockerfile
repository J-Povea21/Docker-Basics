FROM python:3.10-alpine

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV UVICORN_HOST=0.0.0.0

CMD [ "uvicorn", "src.main:app","--proxy-headers", "--reload"]