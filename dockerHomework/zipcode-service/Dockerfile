FROM python:3.9-alpine
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY app.py /app
ENTRYPOINT python app.py
