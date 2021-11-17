FROM python:3.8-slim-buster
ENV DEBUG=True

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY:-cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag}

WORKDIR /app

COPY . .

VOLUME my-vol

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "manage.py"]