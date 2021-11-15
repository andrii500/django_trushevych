FROM python:3.9-bullseye
WORKDIR /app
COPY . .
VOLUME db_volume
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir db
# RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

