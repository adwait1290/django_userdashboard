from django.shortcuts import render
from .models import User
# Create your views here.
def dashboard(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'dashboard.html', context)
def admin(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'adminDashboard.html', context)
