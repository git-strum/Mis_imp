from django.urls import path
from . import views

urlpatterns =[   
    path("welcome/", views.welcome, name = "welcome"),
    path("", views.welcome, name = "welcome"),
    path("webp", views.webpage, name = "webp"),
]