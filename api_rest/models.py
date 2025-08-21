from django.db import models


class User(models.Model):
    user_nickname = models.CharField(primary_key=True,max_length=150, unique=True, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.CharField(max_length=128)
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user_nickname} | email: {self.user_email} '

         