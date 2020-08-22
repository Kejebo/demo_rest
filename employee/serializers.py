from rest_framework import serializers, pagination
from .models import Departament,Skill,Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')

class PersonPagination(pagination.PageNumberPagination):
    page_size = 4
    max_page_size=100
    
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('__all__')


class DeparmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('__all__')
        
class EmployeeSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'type_job',
            'departament',
            'skill',
            )
        extra_kwargs={
            "skill":{"view_name":"app_employee:skill-detail","lookup_field":"pk"},
            "departament":{"view_name":"app_employee:department-detail","lookup_field":"pk"}
        }
        
class EmployeeSerializerTwo(serializers.ModelSerializer):
    skill=SkillSerializer(many=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'type_job',
            'departament',
            'skill',
            )