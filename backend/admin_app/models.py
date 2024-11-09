from django.db import models
from django.conf import settings
from rest_framework.serializers import ValidationError


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_profile')
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    joining_date = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(
        upload_to='admin_profiles/', blank=True, null=True)
    gender = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=15)
    dob = models.DateField(default='2002-08-20')

    class Meta:
        db_table = 'admin'

    def save(self, *args, **kwargs):
        # Check if an Admin instance already exists
        if not self.pk and Admin.objects.exists():
            raise ValidationError("Only one admin instance is allowed.")
        super().save(*args, **kwargs)
