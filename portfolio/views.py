from django.shortcuts import render
from django.views import View
from . import views
from .views import *
# Create your views here.

class PortfolioView(View):
    def get(self, request):
        return render(request, "portfolio/index.html")