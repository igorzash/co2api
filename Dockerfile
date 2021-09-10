FROM python:3.9-buster as setup
WORKDIR /usr/app
COPY init_db.py .
COPY db db
RUN python init_db.py

FROM python:3.9-buster as runtime
WORKDIR /usr/app
COPY --from=setup /usr/app/co2.db .
COPY src src
COPY tests tests
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pytest
CMD [ "sh", "-c", "uvicorn --host 0.0.0.0 --port $PORT src.app:app" ]
