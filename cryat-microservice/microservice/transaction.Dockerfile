FROM CRYAT/base:1.0.3

WORKDIR /CRYAT/transactions

COPY transactions/ .

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8002

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]