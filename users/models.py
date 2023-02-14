'''
1 условие : в приложении юзер не должно быть иных ранее сделанных миграций
2 условие : в settings AUTH_USER_MODEL = 'users.User_model

'''

from django.db import models
from django.contrib.auth.models import AbstractUser


# расширение кастомной юзер модели
class User_model(AbstractUser):
    adress = models.CharField(max_length=100)

    class Meta():
        db_table = 'Users'


# расширение еще одну модуль со связью один к многим (если уже существует много юзеров в бд)
# class Author(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Ім\'я')
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE())