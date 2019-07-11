from django import forms
from .models import Patient,Donor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': 'your aadhar card no.',
        }

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            'name',
            'dob',
            'gender',
            'blood_group',
            'blood_bank',
            'contact_no',
            'address'
        ]
        # fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name',
            'dob',
            'gender',
            'blood_group',
            'disease',
            'contact_no',
            'address'
        ]

class BloodGroup(forms.Form):
    blood_group_choices = [('A+','A+'),('A-','A-'),('B+','B+')
        ,('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')]
    blood_group = forms.ChoiceField(choices = blood_group_choices)