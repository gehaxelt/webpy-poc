FROM python:3.12

RUN pip3 install web.py uwsgi

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

USER appuser
WORKDIR /app/

CMD uwsgi --http :8080 --wsgi-file app.py --master --processes 2 --threads 4