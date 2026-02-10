from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            min_side = min(img.width, img.height)
            left = (img.width - min_side) // 2
            top = (img.height - min_side) // 2
            right = left + min_side
            bottom = top + min_side
            img = img.crop((left, top, right, bottom))
            img = img.resize((300, 300), Image.LANCZOS)
            img.save(self.photo.path)


# Create your models here.
class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField()
    vin_code = models.CharField(max_length=17)
    client_name = models.CharField()
    cover = models.ImageField(upload_to='covers', null=True, blank=True)
    description = HTMLField(verbose_name="Description", max_length=3000, default="")


    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"

    def __str__(self):
        return f"{self.make} {self.model}"

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL,
                            null=True, blank=True, related_name='orders')

    STATUS = (
        ('p', 'Priimtas'),
        ('v', 'Vykdomas'),
        ('t', 'Testuojama'),
        ('u', 'Užbaigtas'),
        ('a', 'Atšauktas')
    )
    status = models.CharField(choices=STATUS, default='p')
    due_date = models.DateField(null=True, blank=True)
    client = models.ForeignKey(to='autoservice.CustomUser', verbose_name="Client", on_delete=models.SET_NULL, null=True, blank=True)

    def is_overdue(self):
        return self.due_date and timezone.now().date() > self.due_date

    def total(self):
        result = 0
        for line in self.lines.all():
            result += line.line_sum()
        return result

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"

    def __str__(self):
        return f"{self.car} {self.date} - {self.total()}"

class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE, related_name="lines")
    service = models.ForeignKey(to="Service",
                                on_delete=models.SET_NULL,
                                null=True, blank=True)
    quantity = models.IntegerField()

    def line_sum(self):
        return self.service.price * self.quantity

    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymo eilutė"

    def __str__(self):
        return f"{self.service.name} ({self.service.price}) * {self.quantity} = {self.line_sum()}"

class OrderReview(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.SET_NULL,
                              null=True, blank=True,
                              related_name="reviews")
    reviewer= models.ForeignKey(to='autoservice.CustomUser', on_delete=models.SET_NULL,
                                null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-date_created']
