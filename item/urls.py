from django.urls import path
from . import views

urlpatterns = [
  path('addItem', views.AddItem.as_view()),
  path('get/<int:itemnumber>', views.GetItem.as_view()),
  path('get', views.GetItems.as_view()),
  path('getSection/<int:sectionnumber>', views.GetItemsWithSection.as_view()),
]
