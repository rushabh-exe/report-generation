from django.shortcuts import render
from .models import Mprodcutions

def reports(request):
    context = {
        'Mproductions': Mprodcutions.objects.all()
    }
    return render(request, 'reports.html', context)
