from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField(max_length=100,primary_key=True)
    student_age=models.IntegerField()


    def __str__(self) -> str:
        return self.student_name