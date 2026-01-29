from django.shortcuts import render

from .models import Service, Order, Car


def index(request):
    context = {
        "num_service": Service.objects.count(),
        "num_order": Order.objects.count(),
        "num_car": Car.objects.count(),
    }

    return render(request, template_name='index.html', context=context)
