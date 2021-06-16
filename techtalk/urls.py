from django.urls import path
from techtalk import views
urlpatterns = [
    path("", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout')
]
