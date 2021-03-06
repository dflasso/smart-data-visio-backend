"""smartDataVisioBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include( ('Security.urls', 'security'), namespace='security' )),
    path('', include( ('patients.urls', 'patients'), namespace='patients' )),
    path('', include( ('classic_test.urls', 'classic_test'), namespace='classic_test' )),
    path('', include( ('ophthalmological_test.urls', 'ophthalmological_test'), namespace='ophthalmological_test' )),
    path('', include( ('legal_documents.urls', 'legal_documents'), namespace='legal_documents' )),
    path('', include( ('reports.urls', 'reports'), namespace='reports' )),
    path('', include( ('questionnaires.urls', 'questionnaires'), namespace='questionnaires' )),
    path('', include( ('virtual_task.urls', 'virtual_task'), namespace='virtual_task' )),
    path('', include( ('analytics.urls', 'analytics'), namespace='analytics' )),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    