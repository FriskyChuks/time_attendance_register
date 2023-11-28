from django.urls import path

from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('clock_in/',clock_in_view,name='clock_in'),
    path('clock_out/',clock_out_view,name='clock_out'),
    path('attendance_records/',attendance_records_view,name='attendance_records'),
]