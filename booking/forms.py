from django import forms
from .models import Appointment, Category, Doctor


class AppointmentForm(forms.ModelForm):
    """Bemor navbat olish formasi"""
    class Meta:
        model = Appointment
        fields = ['patient_first_name', 'patient_last_name', 'patient_phone']
        widgets = {
            'patient_first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingizni kiriting'
            }),
            'patient_last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiyangizni kiriting'
            }),
            'patient_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqamingizni kiriting'
            }),
        }
        labels = {
            'patient_first_name': 'Ism',
            'patient_last_name': 'Familiya',
            'patient_phone': 'Telefon raqami',
        }


class CategoryForm(forms.ModelForm):
    """Kategoriya formasi (admin uchun)"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class DoctorForm(forms.ModelForm):
    """Shifokor formasi (admin uchun)"""
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'category', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
