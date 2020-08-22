from django.contrib import admin
from .models import Employee,Departament,Skill


admin.site.register(Skill)
admin.site.register(Departament)
admin.site.register(Employee)