from django.db import models
from django.urls import reverse


class Users(models.Model):
    user_first_name = models.CharField(max_length=200, verbose_name='Имя пользователя')
    user_last_name = models.CharField(max_length=200, verbose_name='Фамилия пользователя')
    company_name = models.CharField(max_length=250, verbose_name='Название компании')
    email = models.EmailField(max_length=100, verbose_name='Email')

    def __str__(self):
        return f'{self.user_first_name} {self.user_last_name} ({self.company_name})'

    def get_absolute_url(self):
        return reverse('user_detail', kwargs=[str(self.id)])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Clients(models.Model):
    client_first_name = models.CharField(max_length=200, verbose_name='Имя клиента')
    client_last_name = models.CharField(max_length=200, verbose_name='Фамилия клиента')
    client_email = models.EmailField(max_length=100, verbose_name='Email')
    company_name = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользуется услугами компании')

    def __str__(self):
        return f'{self.client_first_name} {self.client_last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
