"""
URL configuration for studymart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include



# from django.urls import path
# # from machine_learning import views
# from machine_learning import views as ml
# from blog import views as b
# from Deep_learning import views as dpl
# from Data_Analysis import views as da
# from About_Us import views as abt
# from machine_learning.views import deep_learning
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/',include('machine_learning.urls')),
    path('dl/',include('Deep_learning.urls')),
    path('data/',include('Data_Analysis.urls')),
    path('blog/',include('blog.urls')),
    path('ab/',include('About_Us.urls')),


    # path('',ml.machine_learning),
    # # path('dl',ml.deep_learning),
    # path('blog',b.blog1),
    # path('deepl',dpl.deep_learning),
    # path('analysis',da.data_analysis),
    # path('aboutus',abt.about_us),
    # path('dl',deep_learning),



]
