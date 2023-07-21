from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import VehicleSearchForm, OrderVehicleForm
from .models import CarType, Vehicle, MembersName


def homepage(request):
  cartype_list = CarType.objects.all().order_by('id')
  # here we are rendering hompage.html file with cartype_list variable consisting all the car type objects
  return render(request, 'carapp/homepage.html', {'cartype_list': cartype_list}) 

def aboutus(request):
  return render(request, 'carapp/aboutus.html') 

def vehicles(request):
  vehicles = Vehicle.objects.all()
  return render(request, 'carapp/vehicles.html', {'vehicles': vehicles})

def cardetail(request, cartype_no):
  car_type = get_object_or_404(CarType, id=cartype_no)
  vehicles = Vehicle.objects.filter(car_type= cartype_no)
  #here we are passing 3 variables
  #1. car_type: for name of car_type
  #2. cartype_no: for id of CarType which will return us number
  #3. vehicles: for name of vehicles associated with car type
  return render(request, 'carapp/cardetail.html', {'car_type': car_type, 'cartype_no': cartype_no, 'vehicles': vehicles}) 

# def members(request):
#   response = HttpResponse()
#   members = MembersName.objects.all()
#   for member in members:
#     para = '<p>' + str(member.first_name) + ' ' + str(member.last_name) + '<br> Link: '+ str(member.link) +'</p>'
#     response.write(para)
#   return response

class TeamMembersView(View):

  def get(self, request):
    team_members = MembersName.objects.all()
    return render(request, 'carapp/team_members.html', {'team_members': team_members})

def vehicle_search(request):
  if request.method == 'POST':
    form = VehicleSearchForm(request.POST)
    if form.is_valid():
      selected_vehicle = form.cleaned_data['vehicle']
      price = selected_vehicle.car_price
      return render(request, 'carapp/search.html', {'form': form, 'price': price})
  else:
    form = VehicleSearchForm()
  return render(request, 'carapp/search.html', {'form': form})

def orderhere(request):
  vehicles = Vehicle.objects.all()
  if request.method == 'POST':
      form = OrderVehicleForm(request.POST)
      if form.is_valid():
        order = form.save(commit=False) 
        if order.vehicle_id.inventory >= order.number_order_vehicle:
          # pdb.set_trace()
          order.save()  # Save the form data to the Order model 
          vehicle = order.vehicle_id
          vehicle.inventory -= order.number_order_vehicle
          vehicle.save()
          return render(request, 'carapp/success_order.html')
        else:
          return render(request, 'carapp/nosuccess_order.html')
  else:
    form = OrderVehicleForm()
  return render(request, 'carapp/order.html', {'form': form, 'vehicles': vehicles})
