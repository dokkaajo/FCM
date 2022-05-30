from django.contrib import admin
from .models import citoyen,CvCitoyen
from comptes.models import Employee
# Register your models here.
admin.site.register(citoyen),
admin.site.register(CvCitoyen)


