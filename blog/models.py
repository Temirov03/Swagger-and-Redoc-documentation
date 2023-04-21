from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nomi')
    model = models.CharField(max_length=255, verbose_name='madel')



    def __str__(self):
        return self.name



    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'
