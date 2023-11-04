from django import forms
from .models import Student, Hostel

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Name', 'Reg_no', 'Mobile_no', 'Student_email', 'Intake_year']

class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ['student', 'Student_stay', 'Members_in_room']
