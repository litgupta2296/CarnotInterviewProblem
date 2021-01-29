from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(label="first name",max_length=20,required=False)
    last_name = forms.CharField(label="last name",max_length=25,required=False)
    student_id = forms.IntegerField(label='student_id',required=False)