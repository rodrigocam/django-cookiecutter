from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label=_('Confirm Password'),
        max_length=50,
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            self.add_error('confirm_password', _("Passwords do not match!"))
        if User.objects.filter(username=username):
            self.add_error('username', _("User already exists!"))

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
