from django.db import models
from django.utils import timezone
import random
import string

class Course(models.Model):
    LEVEL_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    course_name = models.CharField(max_length=255, unique=True)
    course_code = models.CharField(max_length=10, unique=True, editable=False)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    total_marks = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.course_code:
            self.course_code = self.generate_course_code()
        super().save(*args, **kwargs)

    def generate_course_code(self):
        random_chars = ''.join(random.choices(string.ascii_uppercase, k=3))
        random_numbers = str(random.randint(1, 999)).zfill(3)
        course_code = f'{self.course_name[:3].upper()}{random_chars}{random_numbers}'
        return course_code
