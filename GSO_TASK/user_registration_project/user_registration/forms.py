# forms.py

from django import forms
from .models import UserProfile, Hobby

class UserProfileForm(forms.ModelForm):
    hobbies = forms.ModelMultipleChoiceField(queryset=Hobby.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'dob', 'hobbies', 'gender', 'address', 'remark', 'email', 'mobile_number', 'password']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect,
        }
