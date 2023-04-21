from django.db import models

# Create your models here.

class Metto(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    model = models.CharField(max_length=255, verbose_name='madel')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Telefon'
        verbose_name_plural = 'Telefonlar'


class iPhone(models.Model):
    name = models.CharField(max_length=25, verbose_name='Nomi')
    summa = models.IntegerField(default=0)



    def __str__(self):
        return self.name



    class Meta:
        verbose_name = 'iPhone'
        verbose_name_plural = 'iPhonelar'