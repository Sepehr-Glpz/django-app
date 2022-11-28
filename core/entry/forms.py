import django.forms as forms
from .models import EntryRequest
from management.models import ManagementUser
from django.contrib.auth.hashers import make_password


class RequestForm(forms.ModelForm):
    class Meta:
        model = EntryRequest
        fields = [
            'email'
        ]


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ManagementUser
        fields = [
            "name", "username", "email", "national_code", "birth_date", "password",
        ]

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password do not match"
            )


    def save(self, commit=True):
        user = super().save()
        user.password = make_password(self.cleaned_data['password'])
        return user.save()