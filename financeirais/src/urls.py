"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from financeiro.views import images_view
from src import settings

admin.site.site_header = "Módulo FinanceirAIS"
admin.site.site_title = "Portal Administrativo FinanceirAIS"
admin.site.index_title = "FinanceirAIS"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('anexos/', images_view),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
