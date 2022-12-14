from django.urls import path
from . import views

urlpatterns = [
  path('register', views.Register.as_view()),
  path('login', views.Login.as_view()),
  path('logout', views.Logout.as_view()),
  path('get', views.GetUser.as_view()),

  path('chk', views.chk.as_view()),
  path('gett/<int:usernumber>', views.getToken.as_view()),
  path('getu/<int:usernumber>', views.getU.as_view()),

  path('verifyEmail', views.verifyEmail.as_view()),
  path('verifyNickname', views.verifyNickname.as_view()),
]
