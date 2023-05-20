from django.db import models

class Resident(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(choices=[("m", "Male"), ("f", "Female")], default="m", max_length=1)
    adress = models.CharField(max_length=100)
    id_card = models.CharField(max_length=4)


class Enrollment(models.Model):
    enroll_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Resident, on_delete=models.PROTECT)
    symptom = models.TextField(max_length=500)


class DiagnosticResult(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.PROTECT)
    ind_1 = models.FloatField()
    ind_2 = models.FloatField()
