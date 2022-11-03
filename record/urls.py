from django.urls import path
from . import views

urlpatterns = [
  path('addRecord', views.AddRecord.as_view()),
  path('get', views.GetRecords.as_view()),
]
