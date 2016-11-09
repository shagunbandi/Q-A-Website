from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'classWithPad'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'classWithPad'}),
            'email': forms.TextInput(attrs={'class': 'classWithPad'}),
        }


class UpdateProfile(forms.ModelForm):
    keyword = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'classWithPad'}))

    class Meta:
        model = User
        fields = ['username', 'is_staff']
        labels = {
            'is_staff': _('Want to become an admin'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'classWithPad'}),
        }
        error_messages = {
            'keyword': _("This writer's name is too long."),
        }
