from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.homepage, name=""),
    
    path(route="register", view=views.register, name="register"),
    
    path(route="login", view=views.my_login, name="login"),
    
    path(route="dashboard", view=views.dashboard, name="dashboard"),
    
]