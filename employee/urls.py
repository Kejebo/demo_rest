from django.urls import path, re_path

from . import views

app_name = 'app_employee'

urlpatterns = [
    path(
        'api/employee/list/',
        views.EmployeeAPIView.as_view(),
    ),
    path(
        'api/employee/list/<pk>',
        views.EmployeeAPIViewLink.as_view(),
    ),

    path(
        'api/department/list/',
        views.DeparmentAPIView.as_view(),
    ),

    path(
        'api/skill/list/',
        views.SkillAPIView.as_view(),
    ),


    path(
        'api/employee/create/',
        views.EmployeeCreateView.as_view(),
    ),
    path(
        'api/skill/create/',
        views.SkillCreateView.as_view(),
    ),
    path(
        'api/department/create/',
        views.DepartmentCreateView.as_view(),
    ),

    path(
        'api/employee/detail/<pk>',
        views.EmployeeDetailAPIView.as_view()),

    path(
        'api/skill/detail/<pk>',
        views.SkillDetailAPIView.as_view(),
        name='skill-detail'
    ),

    path(
        'api/department/detail/<pk>',
        views.DepartmentDetailAPIView.as_view(),
        name='department-detail'
    ),
    path(
        'api/employee/delete/<pk>',
        views.EmployeeAPIDeleteView.as_view(),
    ),
    path(
        'api/employee/update/<pk>',
        views.EmployeeUpdateView.as_view(),
    ),
    path(
        'api/employee/delete/<pk>',
        views.EmployeeAPIDeleteView.as_view(),
    ),

]
