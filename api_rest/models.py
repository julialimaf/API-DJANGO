from django.db import models


class User(models.Model):
    user_nickname = models.CharField(primary_key=True,max_length=150, unique=True, default='')
    user_email = models.CharField(max_length=128)
    user_age = models.IntegerField(default=0)
    user_password = models.CharField(max_length=128, default='')
    user_cpf = models.CharField(max_length=20, default='')
    user_phone = models.CharField(max_length=15, default='')
    user_city = models.CharField(max_length=128, default='')
    user_birthdate = models.DateField(null=True, blank=True)


    def __str__(self):
        return f'{self.user_nickname} | email: {self.user_email} | age: {self.user_age} | cpf: {self.user_cpf} | phone: {self.user_phone} | city: {self.user_city} | birthdate: {self.user_birthdate} | password: {self.user_password}   '

         