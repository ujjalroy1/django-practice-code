from django.http import HttpResponse
from django.shortcuts import render
from About_Us.models import Teacher
# Create your views here.
def about_us(request):
    return render(request,'about_us/about_us.html')
def teacher_info(request):
    teach=Teacher.objects.all()
    return render(request,'about_us/t.html',{'thr':teach})