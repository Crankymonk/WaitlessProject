from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'table_id', 'room']


class CallCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_id', 'room']
