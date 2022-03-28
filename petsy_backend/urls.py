
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('auth/',include('djoser.social.urls')),

    path('allpets/',include('allpets.urls')),
    path('allusers/',include('allusers.urls')),
]
