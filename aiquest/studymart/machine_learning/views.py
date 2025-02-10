from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine_learning(request):
    # return HttpResponse('hello vai koto try')
    name="Ujjal"
    tm=10
    tp=60
    dy="15 days"
    dic={'what':'second call','times':tm,'topic':tp,'days':dy,'name':name,'names':['Ujjal','roy','Ujjal']}
    return render(request,'machine_learning/machine_learning.html',context=dic)
def deep_learning(request):
    return render('this is deep learning section')
def random(request):
    return render(request,'machine_learning/random_forest.html')
def K_nearest(request):
    return render(request,'machine_learning/knn.html')
def dtree(request):
    return render(request,'machine_learning/DT.html')
