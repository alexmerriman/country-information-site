from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("languages/", views.languages, name="languages"),
    path("references/", views.references, name="references"),
    path("flag/", views.flag, name="flag"),
]

