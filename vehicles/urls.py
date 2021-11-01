from django.urls import path
from django.views.generic import TemplateView
from vehicles.views import vehList
from vehicles.views import vehAdd
from vehicles.views import vehUpdate
from vehicles.views import vehDel
from vehicles.views import vehDetail

urlpatterns = [
    path('', vehList.as_view(), name='index'),
    path('list/', vehList.as_view(), name='list'),
    path('add/', vehAdd.as_view(), name='add'),
    path('update/', vehUpdate.as_view(), name='update'),
    path('delete/', vehDel.as_view(), name='delete'),
    path('details/', vehDetail.as_view(), name='details'),
]
