# django_project/users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    address = forms.CharField()
    country = forms.CharField()
    birthDate = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', "address", "country", "birthDate"]

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        user.country = self.cleaned_data['country']
        user.birthDate = self.cleaned_data['birthDate']
        if commit:
            user.save()
        return user
