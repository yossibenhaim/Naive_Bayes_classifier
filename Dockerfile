FROM python:3

WORKDIR /app

COPY . /app

RUN mkdir -p /app/server/data/storage
RUN chmod -R 777 /app/server/data/storage


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","server.api.server:app","--host", "0.0.0.0", "--port","8000"]