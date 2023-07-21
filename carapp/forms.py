from django import forms

from carapp.models import OrderVehicle, Vehicle, Buyer


class OrderVehicleForm(forms.ModelForm):  
  class Meta:
    model = OrderVehicle
    fields = ['buyer_id', 'vehicle_id', 'number_order_vehicle']

  number_order_vehicle = forms.IntegerField(
    label='Number of Vehicles Ordered'
  )

  buyer_id = forms.ModelChoiceField(
    queryset=Buyer.objects.all(), label='Buyer'
  )

  vehicle_id = forms.ModelChoiceField(
    queryset=Vehicle.objects.all(), label='Vehicle'
  )

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  subject = forms.CharField(max_length=200)
  message = forms.CharField(widget=forms.Textarea)

class VehicleSearchForm(forms.Form):
  vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), empty_label=None)