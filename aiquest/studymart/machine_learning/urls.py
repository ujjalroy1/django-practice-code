
from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.machine_learning),
    path('dl',views.deep_learning),
    path('rn/',views.random),
    path('knn/',views.K_nearest),
    path('dt',views.dtree),
]
