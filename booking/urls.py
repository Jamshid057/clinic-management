from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.doctor_list_by_category, name='doctor_list'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('appointment/<int:appointment_id>/success/', views.appointment_success, name='appointment_success'),
]
