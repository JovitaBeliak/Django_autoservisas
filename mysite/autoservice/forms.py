from .models import OrderReview, CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ['content']

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'photo']