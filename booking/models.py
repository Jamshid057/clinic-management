from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Kategoriya nomi")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="doctors",
        verbose_name="Kategoriya",
    )
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Telefon raqami to'g'ri formatda bo'lishi kerak.",
            )
        ],
        verbose_name="Telefon raqami",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Shifokor"
        verbose_name_plural = "Shifokorlar"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    patient_first_name = models.CharField(max_length=100, verbose_name="Bemor ismi")
    patient_last_name = models.CharField(
        max_length=100, verbose_name="Bemor familiyasi"
    )
    patient_phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Telefon raqami to'g'ri formatda bo'lishi kerak.",
            )
        ],
        verbose_name="Bemor telefon raqami",
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name="Shifokor",
    )
    queue_number = models.PositiveIntegerField(verbose_name="Navbat raqami")
    qr_code_image = models.ImageField(
        upload_to="qr_codes/", blank=True, null=True, verbose_name="QR kod rasmi"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Navbat"
        verbose_name_plural = "Navbatlar"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.patient_first_name} {self.patient_last_name} - {self.doctor.full_name} (#{self.queue_number})"
