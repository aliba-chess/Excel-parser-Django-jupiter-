from django.shortcuts import render
from dashboard.models import DashboardOrder

def myview(request):
    rows = DashboardOrder.objects.all()
    return render(request, "mytemplate.html", {"rows" : rows })