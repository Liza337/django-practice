from django import forms
from .models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"  # je model ache sob field die ekta form
