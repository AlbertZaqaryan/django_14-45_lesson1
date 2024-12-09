"""
URL configuration for shop project.

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
from django.urls import path
from main.views import index, calculator, post_data, calc, calc_get

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
    path('calculator/', calculator),
    path('post_data/<str:name>/<int:age>/', post_data),
    path('calc/<int:number1>/<str:char>/<int:number2>/', calc),
    path('calc_get/', calc_get),
]
