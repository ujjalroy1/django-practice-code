from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog1,name="blog"),
    path('f',views.showformdata),
]
