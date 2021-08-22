from django.urls import path
from . import views


urlpatterns=[
    path("",views.explore,name="explore"),
    path("register",views.register, name="register"),
    path("login",views.login,name="login"),
    path("submit",views.submit,name="submit"),
    path("view1", views.view1,name="view1"),
]