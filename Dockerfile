FROM python:3.9-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow   

COPY .env .

COPY template.png . 

COPY main.py . 

CMD ["python", "main.py"]