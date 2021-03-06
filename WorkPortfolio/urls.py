"""WorkPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import jobs.views #required to show the view
from django.conf import settings #necessary for the static file
from django.conf.urls.static import static  #necessary for the static file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),#for it to work i need to create a file, 
    #it was created in templates/jobs/home.html, and import it, done above
    path('jobs/<int:job_id>', jobs.views.detail, name='detail')#path to the job view
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #after the plus required to show the static file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #after the plus required to media file




