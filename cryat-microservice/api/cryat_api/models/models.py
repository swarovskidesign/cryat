# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser

# class Users(AbstractBaseUser):
#     """
#     Модель пользователя
#     """
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=64, unique=True)
#     favorite_word = models.CharField(max_length=64)
#     password = models.CharField(max_length=128)
#     account_number = models.CharField(max_length=64, unique=True, null=True, blank=True)
#     role = models.CharField(max_length=8, default="user")
#     tg_token = models.CharField(max_length=64, unique=True, null=True, blank=True)
#     email_name = models.CharField(max_length=64, unique=True, null=True, blank=True)
#     last_login = models.GenericIPAddressField(null=True, blank=True)
#     last_active = models.CharField(max_length=16, null=True, blank=True)

#     def __str__(self):
#         return self.username
    
#     def set_password(self, raw_password):
#         return super().set_password(raw_password)
    
# class MetadataforUsers(models.Model):
#     """
#     Модель метаданных для пользователей
#     """
#     user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='metadata')
#     token = models.CharField(max_length=64, unique=True, null=True, blank=True)
#     refresh_token = models.CharField(max_length=64, unique=True, null=True, blank=True)
#     token_expiration = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"Metadata for {self.user.username}"
    
