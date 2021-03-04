from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('admin/', admin.site.urls), #admin, admin1234
    path('articles/', include("articles.urls")),
    path('about/', views.about),
    path('', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
