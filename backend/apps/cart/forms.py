from django import forms
from .models import Cart

# Create your models here.


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
