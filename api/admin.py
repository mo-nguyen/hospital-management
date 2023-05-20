from django.contrib import admin
from .models import Resident, Enrollment, DiagnosticResult

# Register your models here.

admin.site.register(Resident)
admin.site.register(Enrollment)
admin.site.register(DiagnosticResult)