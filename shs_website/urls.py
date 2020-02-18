#i copied the format from the main urls.py file from shs_web_project

"""shs_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="home"),
    path('AboutUS/', views.aboutus, name="aboutus"),
    path('ChairmenDesk/', views.ChairmenDesk, name="ChairmenDesk"),
    path('PrincipalDesk/', views.PrincipalDesk, name="PrincipalDesk"),
    path('Faculty/', views.faculty, name="faculty"),
    path('AddFaculty/', views.AddNewFaculty, name="AddNewFaculty"),
    path('EditFaculty/', views.EditFaculty, name="EditFaculty"),
    path('DeleteFaculty/', views.DeleteFaculty, name="DeleteFaculty"),
    path('UpdateRecord/', views.UpdateRecord, name="UpdateRecord"),
    path('Enquiry/', views.admission_enquiry, name="admission_enquiry"),
    path('ContactUS/', views.contactus, name="contactus"),
    path('LogIN/', views.log_in, name="login"),
    path('LogOUT/', views.log_out, name="logout"),
    path('AdmissionProcedure/', views.admission_procedure, name="admission_procedure"),
    path('Notifications/', views.notifications, name="notifications"),
    path('DeleteNotification/', views.DeleteNotification, name="DeleteNotification"),
    path('Events/', views.event_detail, name="event_detail"),
    path('DeleteEvent/', views.DeleteEvent, name="DeleteEvent"),
    path('AddPost/', views.AddPost, name="AddPost"),
    path('gallery/', views.gallery, name="gallery"),
    path('Career/', views.career, name="career"),
    path('Test/', views.Test, name="Test"),

]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

