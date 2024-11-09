from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('admin', 'Admin')
    )

    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='user')
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expiry = models.DateTimeField(null=True, blank=True)
    max_otp_try = models.IntegerField(default=3)
    otp_max_out = models.DateTimeField(null=True, blank=True)
    password_reset_otp = models.CharField(max_length=6, null=True, blank=True)
    password_reset_otp_expiry = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'  # Use email as the username field
    REQUIRED_FIELDS = ['username']  # Remove email from here if it was present

    def __str__(self):
        return self.email

    def is_otp_valid(self):
        if self.otp and self.otp_expiry:
            return timezone.now() <= self.otp_expiry
        return False

    def can_send_otp(self):
        if self.otp_max_out:
            return timezone.now() > self.otp_max_out
        return self.max_otp_try > 0
