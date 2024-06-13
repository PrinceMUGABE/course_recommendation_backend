from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.conf import settings
from courseApp.models import Course
from userApp.models import User

def get_default_user():
    return settings.AUTH_USER_MODEL.objects.first().pk

class StudentRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.rol_no} - {self.course.course_name}"

    def has_failed(self):
        return self.marks < Decimal(0.5) * self.course.total_marks