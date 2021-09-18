"""mdc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include

urlpatterns = [
    #firstly server comes to newproject urls and here thenrecieve
    path('admin/', admin.site.urls),
    #then goes to shop urls and pass shop and here include means pass shop url
    path('shop/',include('shop.urls')),
    #and then if you writr blog on serve   the function goes to here then proceed
    path('blog/',include('blog.urls'))
   

]
