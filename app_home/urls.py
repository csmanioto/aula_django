from django.urls import path
from .views import show_players, home_view

urlpatterns = [
    path('show_players', show_players),
    path('', home_view, name="home"),
]