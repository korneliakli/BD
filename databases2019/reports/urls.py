from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
        path('', views.generate_report, name='report'),
            
] 