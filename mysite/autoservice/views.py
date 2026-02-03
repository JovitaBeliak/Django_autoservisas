from django.shortcuts import render

from .models import Service, Order, Car
from django.views import generic

def index(request):
    context = {
        "num_service": Service.objects.count(),
        "num_order": Order.objects.filter(status='u').count(),
        "num_car": Car.objects.count(),
    }

    return render(request, template_name='index.html', context=context)

def cars(request):
    context = {
        "cars": Car.objects.all(),
    }
    return render(request, template_name='cars.html', context=context)


def car(request, car_id):
    context = {
        "car": Car.objects.get(id=car_id)
    }
    return render(request, template_name='car.html', context=context)

class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'
