# Doctor Appointment Booking System

Django-da yaratilgan bemorlar uchun masofadan navbat olish tizimi va alohida admin panel.

## Xususiyatlar

- **Bemorlar uchun:**
  - Shifokor kategoriyalarini ko'rish
  - Kategoriya bo'yicha shifokorlarni tanlash
  - Shifokorga navbat olish
  - QR kodli navbat raqami olish

- **Admin panel:**
  - Kategoriyalarni boshqarish (CRUD)
  - Shifokorlarni boshqarish (CRUD)
  - Navbatlarni ko'rish va boshqarish
  - Dashboard statistikasi

## O'rnatish

1. Paketlarni o'rnatish:
```bash
uv sync
```

2. Migratsiyalarni ishga tushirish:
```bash
uv run python manage.py migrate
```

3. Admin user yaratish:
```bash
uv run python manage.py create_admin --username admin --password admin123
```

Yoki o'z parametrlaringiz bilan:
```bash
uv run python manage.py create_admin --username myadmin --email admin@example.com --password mypassword
```

## Ishga tushirish

```bash
uv run python manage.py runserver
```

## URL'lar

- **Bemorlar uchun:**
  - `/` - Kategoriyalar ro'yxati
  - `/category/<id>/` - Kategoriya bo'yicha shifokorlar
  - `/doctor/<id>/` - Shifokor tafsilotlari va navbat olish
  - `/appointment/<id>/success/` - Navbat muvaffaqiyatli yaratilgan sahifa

- **Admin panel:**
  - `/admin-panel/` - Admin login
  - `/admin-panel/dashboard/` - Dashboard
  - `/admin-panel/categories/` - Kategoriyalarni boshqarish
  - `/admin-panel/doctors/` - Shifokorlarni boshqarish
  - `/admin-panel/appointments/` - Navbatlarni ko'rish

## Texnologiyalar

- Django 6.0+
- SQLite (development)
- Bootstrap 5 (UI)
- qrcode (QR kod generatsiya)
- Pillow (rasm ishlash)

## Struktura

```
doctor/
├── booking/          # Bemorlar uchun booking app
├── admin_panel/      # Custom admin panel
├── root/             # Django settings
└── static/           # Static fayllar
```

## Eslatma

- QR kodlar `media/qr_codes/` papkasida saqlanadi
- Admin panel Django'ning default admin panelidan alohida yaratilgan
- Barcha admin sahifalar login talab qiladi
