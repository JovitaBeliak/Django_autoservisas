from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField()
    model = models.FloatField()
    license_plate = models.CharField()
    vin_code = models.CharField(max_length=17)
    client_name = models.CharField()

    def __str__(self):
        return (f"{self.make} {self.model} {self.license_plate}")

class Order(models.Model):
    date = models.DateField()
    car_id = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.date}"

class Order_line(models.Model):
    order_id = models.ForeignKey(to="Order", on_delete=models.SET_NULL, null=True, blank=True)
    service_id = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order_id} {self.service_id} {self.quantity}"