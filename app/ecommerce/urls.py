"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin

from products.views import ProductListView, productlistview
from .views import index, about, contact, register, login

urlpatterns = [
    url(r'^$', index),
    url(r'^about/', about),
    url(r'^contact/', contact),
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^products/', ProductListView.as_view()),
    url(r'^products-func/', productlistview),
    url(r'^admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)