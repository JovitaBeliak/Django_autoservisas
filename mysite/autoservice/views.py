from django.shortcuts import render
from .models import Service, Order, Car
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_service": Service.objects.count(),
        "num_order": Order.objects.filter(status='u').count(),
        "num_car": Car.objects.count(),
        "num_visits": num_visits,
    }

    return render(request, template_name='index.html', context=context)

def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        "cars": paged_cars,
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
    paginate_by = 2


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'


def search(request):
    query = request.GET.get('query')
    context = {
        "cars": Car.objects.filter(Q(make__icontains=query) |
                                   Q(model__icontains=query) |
                                   Q(client_name__icontains=query) |
                                   Q(license_plate__icontains=query) |
                                   Q(vin_code__icontains=query)),
    }
    return render(request, template_name='search.html', context=context)


class MyOrdersListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'my_orders.html'
    context_object_name = 'myorders'

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)

