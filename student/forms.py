from django import forms
from django.db import models
from student.models import *

class facultyform(forms.ModelForm):
    class Meta:
        model=faculty
        fields='__all__'
    def clean_Email(self):
        name=self.cleaned_data.get('Email')
        if faculty.objects.filter(Email=name.lower()):
            raise forms.ValidationError("Faculty already exists..!")
        return name.lower()