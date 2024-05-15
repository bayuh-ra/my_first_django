from django import forms

COURSES =( 
    ("BS-CS", "Computer Science"), 
    ("BS-DS", "Data Science"), 
    ("BS-IT", "Information Technology"), 
    ("BS-IS", "Information System"),
) 

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
)

class StudentForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    course = forms.ChoiceField(choices= COURSES, required= True)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, required=True)
    age = forms.IntegerField(required=True)
    

