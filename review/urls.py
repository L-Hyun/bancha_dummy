from django.urls import path
from . import views

urlpatterns = [
  path('addReview', views.AddReview.as_view()),
  path('get/<int:itemnumber>', views.GetReviews.as_view()),
]
