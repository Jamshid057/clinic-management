from io import BytesIO

import qrcode
from django.conf import settings
from django.core.files import File


def generate_qr_code(appointment):
    """Navbat uchun QR kod yaratish"""
    # QR kod ma'lumotlari
    qr_data = f"Appointment ID: {appointment.id}\n"
    qr_data += f"Doctor: {appointment.doctor.full_name}\n"
    qr_data += (
        f"Patient: {appointment.patient_first_name} {appointment.patient_last_name}\n"
    )
    qr_data += f"Queue Number: {appointment.queue_number}\n"
    qr_data += f"Phone: {appointment.patient_phone}\n"
    qr_data += f"Date: {appointment.created_at.strftime('%Y-%m-%d %H:%M')}"

    # QR kod yaratish
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # QR kod rasmini yaratish
    img = qr.make_image(fill_color="black", back_color="white")

    # BytesIO ga saqlash
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Fayl nomi
    filename = f"qr_code_{appointment.id}.png"

    # ImageField ga saqlash
    appointment.qr_code_image.save(filename, File(buffer), save=False)
    appointment.save()
