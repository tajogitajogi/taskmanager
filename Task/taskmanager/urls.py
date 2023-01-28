from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='main'),
    path('<int:pk>', views.delete,name='delete')
]
