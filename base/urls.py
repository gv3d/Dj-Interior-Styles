from django.contrib import admin
from django.urls import path
from . import views  # from . import - посиання на файл що знаходиться в цій же директорії

urlpatterns = [
    path('', views.home),
]
