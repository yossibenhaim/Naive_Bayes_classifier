FROM python:3

WORKDIR /server

COPY . /server

RUN mkdir -p /server/logs

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","api.server:app","--host", "0.0.0.0", "--port","8000"]