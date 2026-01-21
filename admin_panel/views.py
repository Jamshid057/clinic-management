from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone
from booking.models import Category, Doctor, Appointment
from booking.forms import CategoryForm, DoctorForm
from .forms import AdminLoginForm
from .decorators import admin_required


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:dashboard')

    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_panel:dashboard')
            else:
                messages.error(request, 'Username yoki password noto\'g\'ri!')
    else:
        form = AdminLoginForm()

    return render(request, 'admin_panel/login.html', {'form': form})


@admin_required
def admin_logout(request):
    logout(request)
    return redirect('admin_panel:login')


@admin_required
def admin_dashboard(request):
    stats = {
        'total_categories': Category.objects.count(),
        'total_doctors': Doctor.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'today_appointments': Appointment.objects.filter(
            created_at__date=timezone.now().date()
        ).count(),
    }
    recent_appointments = Appointment.objects.select_related('doctor').order_by('-created_at')[:10]

    return render(request, 'admin_panel/dashboard.html', {
        'stats': stats,
        'recent_appointments': recent_appointments
    })


@admin_required
def admin_categories(request):
    categories = Category.objects.annotate(
        doctor_count=Count('doctors')
    ).all()

    if request.method == 'POST':
        if 'delete' in request.POST:
            category_id = request.POST.get('category_id')
            category = get_object_or_404(Category, id=category_id)
            category.delete()
            return redirect('admin_panel:categories')

    return render(request, 'admin_panel/categories.html', {
        'categories': categories
    })


@admin_required
def admin_category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:categories')
    else:
        form = CategoryForm()

    return render(request, 'admin_panel/category_form.html', {
        'form': form,
        'title': 'Yangi kategoriya'
    })


@admin_required
def admin_category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'admin_panel/category_form.html', {
        'form': form,
        'category': category,
        'title': 'Kategoriyani tahrirlash'
    })


@admin_required
def admin_doctors(request):
    doctors = Doctor.objects.select_related('category').all()

    if request.method == 'POST':
        if 'delete' in request.POST:
            doctor_id = request.POST.get('doctor_id')
            doctor = get_object_or_404(Doctor, id=doctor_id)
            doctor.delete()
            return redirect('admin_panel:doctors')

    return render(request, 'admin_panel/doctors.html', {
        'doctors': doctors
    })


@admin_required
def admin_doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:doctors')
    else:
        form = DoctorForm()

    return render(request, 'admin_panel/doctor_form.html', {
        'form': form,
        'title': 'Yangi shifokor'
    })


@admin_required
def admin_doctor_edit(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:doctors')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'admin_panel/doctor_form.html', {
        'form': form,
        'doctor': doctor,
        'title': 'Shifokorni tahrirlash'
    })


@admin_required
def admin_appointments(request):
    appointments = Appointment.objects.select_related('doctor').order_by('-created_at')

    return render(request, 'admin_panel/appointments.html', {
        'appointments': appointments
    })
