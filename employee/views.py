from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee,Departament,Skill
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateAPIView)
from .serializers import EmployeeSerializer, EmployeeSerializerTwo, DeparmentSerializer,SkillSerializer,EmployeeSerializerLink

class EmployeeAPIView(ListAPIView):
    serializer_class=EmployeeSerializerTwo
    def get_queryset(self):
        return Employee.objects.all()
    
class EmployeeAPIViewTwo(ListAPIView):
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        return Employee.objects.all()

class DeparmentAPIView(ListAPIView):
    serializer_class=DeparmentSerializer
    def get_queryset(self):
        return Departament.objects.all()

class SkillAPIView(ListAPIView):
    serializer_class=SkillSerializer
    def get_queryset(self):
        return Skill.objects.all()

class EmployeeAPIViewLink(RetrieveAPIView):
    serializer_class=EmployeeSerializerLink
    queryset=Employee.objects.filter()
    
class EmployeeDetailAPIView(RetrieveAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.filter()

class SkillDetailAPIView(RetrieveAPIView):
    serializer_class=SkillSerializer
    queryset=Skill.objects.filter()

class DepartmentDetailAPIView(RetrieveAPIView):
    serializer_class=DeparmentSerializer
    queryset=Departament.objects.filter()


class EmployeeCreateView(CreateAPIView):
    serializer_class=EmployeeSerializer
    
class DepartmentCreateView(CreateAPIView):
    serializer_class=DeparmentSerializer

class SkillCreateView(CreateAPIView):
    serializer_class=SkillSerializer
    


class EmployeeAPIDeleteView(DestroyAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

class SkillAPIDeleteView(DestroyAPIView):
    serializer_class=SkillSerializer
    queryset=Skill.objects.all()

class DepartmentAPIDeleteView(DestroyAPIView):
    serializer_class=DeparmentSerializer
    queryset=Departament.objects.all()


class EmployeeUpdateView(RetrieveUpdateAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
