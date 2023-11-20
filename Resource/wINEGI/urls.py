from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("menu/", views.menu, name="menu"),
    path("locality/", views.locality, name="locality"),
]