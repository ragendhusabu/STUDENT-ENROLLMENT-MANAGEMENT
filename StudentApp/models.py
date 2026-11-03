from django.db import models



# Create your models here.
class StudentDb(models.Model):
    student_name = models.CharField(max_length=100)
    email =models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    joining_date =models.DateField()


    def __str__(self):
        return self.student_name

class EnrollmentDb(models.Model):
    student = models.ForeignKey(StudentDb,on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    enrollment =models.DateField()
    duration = models.IntegerField()
    status = models.CharField(max_length=20,default="active")

    def __str__(self):
        return f"{self.student.student_name} - {self.course}"