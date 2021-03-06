FROM python:3.9-bullseye
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "manage.py", "runserver 0.0.0.0:8000"]
