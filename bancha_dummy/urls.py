from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('user/', include('user.urls')),
  path('item/', include('item.urls')),
  # path('record/', include('record.urls')),
  # path('review/', include('review.urls')),
]
