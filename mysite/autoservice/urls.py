from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>/', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order'),
    path('search/', views.search, name='search'),
    path('myorders/', views.MyOrdersListView.as_view(), name="myorders"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('orders/create/', views.MyOrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', views.MyOrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', views.MyOrderDeleteView.as_view(), name='order_delete'),
]