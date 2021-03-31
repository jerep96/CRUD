from django.db import models


# Create your models here.
class Client (models.Model):
    client_name = models.CharField('Name', max_length=20)
    client_lastname = models.CharField('Lastname', max_length=20)
    client_address = models.CharField('Address', max_length=50)


class Login (models.Model):
    user_name = models.CharField('Username', max_length=20, primary_key=True)
    password = models.CharField('Password', max_length=20)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
