from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.PortfolioView.as_view(), name="home"),
]
