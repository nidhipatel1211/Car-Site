from django.urls import path

from . import views
from .views import TeamMembersView

urlpatterns = [
  path("", views.homepage, name="homepage"),
  path("aboutus/", views.aboutus, name="aboutus"),
  path("<int:cartype_no>/", views.cardetail, name="cardetail"),
  # path("members/", views.members, name="members"),
  path('team-members/', TeamMembersView.as_view(), name='team_members'),
  path("vehicles/",  views.vehicles, name='vehicles'),
  path("order/",  views.orderhere, name='order'),
  path("search/", views.vehicle_search, name='search')
]