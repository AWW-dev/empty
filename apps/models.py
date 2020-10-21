from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=250, verbose_name="nazwa")
    content = models.CharField(max_length=250, verbose_name="opis aplikacji")
    price = models.IntegerField(verbose_name="cena")
    create_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=100, verbose_name="link")

    def __str__(self):
        return f"Nazwa aplikacji {self.name} - opis: {self.content}, cena: {self.price}, link: {self.link}"

