from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import Teachersregistration
# Create your views here.
def blog1(request):
     return render(request,'blogs/blogs.html')

def showformdata(request):
     fm=Teachersregistration()
     return render(request,'blogs/forms.html',{'form':fm})
