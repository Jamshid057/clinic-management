from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Max
from django.utils import timezone
from .models import Category, Doctor, Appointment
from .forms import AppointmentForm
from .utils import generate_qr_code


def category_list(request):
    """Barcha kategoriyalarni ko'rsatish"""
    categories = Category.objects.annotate(
        doctor_count=Count('doctors')
    ).all()
    return render(request, 'booking/category_list.html', {
        'categories': categories
    })


def doctor_list_by_category(request, category_id):
    """Kategoriya bo'yicha shifokorlar ro'yxati"""
    category = get_object_or_404(Category, id=category_id)
    doctors = Doctor.objects.filter(category=category)
    return render(request, 'booking/doctor_list.html', {
        'category': category,
        'doctors': doctors
    })


def doctor_detail(request, doctor_id):
    """Shifokor tafsilotlari va navbat olish formasi"""
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Navbat raqamini hisoblash
            today = timezone.now().date()
            today_appointments = Appointment.objects.filter(
                doctor=doctor,
                created_at__date=today
            )
            # Agar bugungi sana bo'yicha navbatlar bo'lsa, eng katta raqam + 1
            if today_appointments.exists():
                max_queue = today_appointments.aggregate(
                    max_queue=Max('queue_number')
                )['max_queue'] or 0
                queue_number = max_queue + 1
            else:
                queue_number = 1
            
            # Appointment yaratish
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.queue_number = queue_number
            appointment.save()
            
            # QR kod generatsiya qilish
            generate_qr_code(appointment)
            
            return redirect('booking:appointment_success', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    
    return render(request, 'booking/doctor_detail.html', {
        'doctor': doctor,
        'form': form
    })


def appointment_success(request, appointment_id):
    """Navbat muvaffaqiyatli yaratilgan sahifa"""
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'booking/appointment_success.html', {
        'appointment': appointment
    })
