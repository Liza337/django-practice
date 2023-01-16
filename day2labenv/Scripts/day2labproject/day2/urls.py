from django.urls import path
from .views import CreateEmployee,GetEmployee,DeleteEmployee,Home
urlpatterns = [
 path('', Home, name='home'),
 path('create', CreateEmployee, name='create_new_emp'),
 path('emp_edit/<str:idt>/', GetEmployee, name='emp_edit'),
 path('delete/<str:idt>', DeleteEmployee, name='delete'),
 #path('delete/<str:idt>', AddNewEmployee, name='Addnew'),

]
