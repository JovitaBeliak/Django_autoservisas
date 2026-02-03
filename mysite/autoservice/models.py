from django.db import models

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

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"

    def __str__(self):
        return (f"{self.make} {self.model}")

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