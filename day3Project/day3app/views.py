from django.shortcuts import render


# Create your views here.
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee


class EmployeeBaseView(View):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('day3app:all')


class EmployeeListView(EmployeeBaseView, ListView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('day3app:all')


class EmployeeDetailView(EmployeeBaseView, DetailView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('day3app:all')


class EmployeeCreateView(EmployeeBaseView, CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('day3app:all')


class EmployeeUpdateView(EmployeeBaseView, UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('day3app:all')


class EmployeeDeleteView(EmployeeBaseView, DeleteView):
    model = Employee
    # fields = '__all__'
    success_url = reverse_lazy('day3app:all')
