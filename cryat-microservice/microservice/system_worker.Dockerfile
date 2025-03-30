FROM python3.9:slim

WORKDIR /CRYAT/system-worker

COPY system_worker/ .

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8005

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
