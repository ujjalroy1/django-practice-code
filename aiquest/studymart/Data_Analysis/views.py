from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data_analysis(request):
    return render(request,'analysis/analysis.html')
