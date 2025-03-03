FROM CRYAT/base:1.0.3

WORKDIR /CRYAT/user_manager

COPY user_manager/ .

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8003

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]