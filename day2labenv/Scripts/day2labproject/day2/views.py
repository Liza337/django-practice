from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from .forms import CreateEmployeeForm
from .models import Employee
def Home(request):
    employees = Employee.objects.all()
    context = { 'employees': employees}
    return render(request, 'index.html', context)

def CreateEmployee(request):
             if request.method == "POST":
                 form = CreateEmployeeForm(request.POST)
                 if form.is_valid():
                   form.save()
                   #form = CreateEmployeeForm()
                 return redirect(Home)

             else:
               form = CreateEmployeeForm()

             employees = Employee.objects.all()
             context = {'form':form, 'employees':employees}
             return render(request, 'addnew.html',context)


def DeleteEmployee(request, **kwargs):
    idt = kwargs.get('idt')
    employee = Employee.objects.get(emp_id=idt)
    employee.delete()
    return redirect(Home)

def GetEmployee(request, **kwargs):
    idt = kwargs.get('idt')
    employee = get_object_or_404(Employee, emp_id=idt)
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(Home)

    else:
            form = CreateEmployeeForm(instance=employee)
            context = {'employee':employee, 'form': form}
    return render(request, 'emp_edit.html', context )

