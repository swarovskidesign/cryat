from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    """
    Модель пользователя
    Хранит информацию о пользователе
    """
    email = None
    first_name = None
    last_name = None

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    favorite_word = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    account_number = models.CharField(max_length=64, unique=True, null=True, blank=True)
    role = models.CharField(max_length=8, default="user")
    tg_token = models.CharField(max_length=64, unique=True, null=True, blank=True)
    email_name = models.CharField(max_length=64, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        return super().set_password(raw_password)
    
class MetadataforUsers(models.Model):
    """
    Модель метаданных для пользователей
    Хранит токены для аутентификации и обновления
    """
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='metadata')
    token = models.CharField(max_length=64, unique=True, null=True, blank=True)
    refresh_token = models.CharField(max_length=64, unique=True, null=True, blank=True)
    token_expiration = models.DateTimeField(null=True, blank=True)
    last_login = models.GenericIPAddressField(null=True, blank=True)
    last_active = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return f"Metadata for {self.user.username}"
    
class Accounts(models.Model):
    """
    Модель счетов пользователей
    Счетов может быть несколько на пользователя
    """
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=64, unique=True)
    account_type = models.CharField(max_length=16, choices=[('savings', 'Savings'), ('fiat', 'Fiat')])
    account_name = models.CharField(max_length=64, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default="USD")
    created_at = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Account {self.account_number} for {self.user.username}"
    
