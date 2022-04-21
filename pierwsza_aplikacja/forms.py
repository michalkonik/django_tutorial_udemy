from dataclasses import field
from click import password_option
from django import forms
from django.core import validators
from django.contrib.auth.models import User
from pierwsza_aplikacja.models import UserProfileInfo


def check_length(value):
    if len(value) < 4:
        raise forms.ValidationError("Name needs to be longer than 3 letters!")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_length])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # it was just an example of how to catch the bot in django. 
    # the below way is only exemplary, as django has built in validators. 
    '''def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA SZMATO RUSKA")
        return botcatcher'''


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
