"""
from django.shortcuts import render
# Create your views here.
from .models import Employee
from .serializer import EmployeeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# List all Employee, or create a new Employee.
class EmployeeList(APIView):
    def get(self, request, format=None):
        Employees = Employee.objects.all()
        serializer = EmployeeSerializer(Employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Retrieve, update or delete a Employee instance.

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Employee = self.get_object(pk)
        serializer = EmployeeSerializer(Employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Employee = self.get_object(pk)
        Employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""


#Using mixins
"""

from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import mixins
from rest_framework import generics

class EmployeeList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)


class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer

     def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)

     def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

     def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)


"""



 #Using generic class-based views

from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import generics

class EmployeeList(generics.ListCreateAPIView):
      queryset = Employee.objects.all()
      serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Employee.objects.all()
      serializer_class = EmployeeSerializer

