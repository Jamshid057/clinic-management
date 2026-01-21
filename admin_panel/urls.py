from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('categories/', views.admin_categories, name='categories'),
    path('categories/add/', views.admin_category_add, name='category_add'),
    path('categories/<int:category_id>/edit/', views.admin_category_edit, name='category_edit'),
    path('doctors/', views.admin_doctors, name='doctors'),
    path('doctors/add/', views.admin_doctor_add, name='doctor_add'),
    path('doctors/<int:doctor_id>/edit/', views.admin_doctor_edit, name='doctor_edit'),
    path('appointments/', views.admin_appointments, name='appointments'),
]
