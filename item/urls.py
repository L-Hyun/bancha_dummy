from django.urls import path
from . import views

urlpatterns = [
  path('addItem', views.AddItem.as_view()),
  path('get/<int:itemnumber>', views.GetItem.as_view()),
]
