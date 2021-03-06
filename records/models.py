from django.db import models
from django.db.models import F
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    name = models.CharField(max_length=40, null=False)
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    CLASSES = (
        ('Baby class', 'Baby class'),
        ('Class 1', 'class 1'),
        ('Class 2', 'class 2'),
        ('Class 3', 'class 3'),
        ('Class 4', 'class 4'),
        ('Class 5', 'class 5'),
        ('Class 6', 'class 6'),
        ('Class 7', 'class 7'),
    )
    name = models.CharField(max_length=40, choices=CLASSES)
    
    def __str__(self):
        return self.name
    
    
class Records(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    classrooms = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
    school_fees = models.FloatField(default=1000000)
    received_fees = models.FloatField(null=False)
    Remaining_fees = models.FloatField(blank=True)
    completed = models.BooleanField(null=False, default=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField(null=True)
    
    def save(self, *args, **kwargs):
        self.Remaining_fees = self.school_fees - self.received_fees
        super().save( *args, **kwargs)
        
        def save(self, *args, **kwargs):
            if self.Remaining_fees == 0:
                
                super().save( *args, **kwargs)