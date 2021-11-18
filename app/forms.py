from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoriesForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class CustomersForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'