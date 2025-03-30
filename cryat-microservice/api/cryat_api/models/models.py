from django.db import models

class Token_users(models.Model):
    id = models.AutoField(primary_key=True)
    

    def __str__(self):
        return self.username