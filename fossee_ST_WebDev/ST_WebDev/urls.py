from django.urls import path
from . import views
app_name='foss'
urlpatterns=[
        path('',views.index,name='index'),
        ]
