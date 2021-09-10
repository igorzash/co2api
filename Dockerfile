FROM python:3.9-buster as setup
WORKDIR /usr/app
COPY init_db.py .
COPY db db
RUN python init_db.py

FROM python:3.9-buster as runtime
WORKDIR /usr/app
COPY --from=setup /usr/app/co2.db .
COPY data data
COPY model model
COPY resources resources
COPY middleware middleware
COPY __init__.py .
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "sh", "-c", "uvicorn --host 0.0.0.0 --port $PORT app:app" ]
