from django import forms
from students.models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"