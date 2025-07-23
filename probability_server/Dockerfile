FROM python:3

WORKDIR /probability_server

COPY . /probability_server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["uvicorn","probability_api.probability_server:app","--host", "0.0.0.0", "--port","8001"]