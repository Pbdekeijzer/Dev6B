"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import DataBaseUser

class BootstrapAuthenticationForm(AuthenticationForm):
    print("at BootstrapAuthenticationForm")
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    username_for_register = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password_for_register = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class DatabaseUserForm(forms.ModelForm):
    class Meta:
        model = DataBaseUser
        fields = ('username', 'password')



#class PostForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        # exclude = ['author', 'updated', 'created', ]
#        fields = ['text']
#        widgets = {
#            'text': forms.TextInput(
#                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
#            ),
#        }