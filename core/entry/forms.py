import django.forms as forms
from .models import EntryRequest
from management.models import ManagementUser


class RequestForm(forms.ModelForm):
    class Meta:
        model = EntryRequest
        fields = [
            'email'
        ]


class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ManagementUser
        exclude = ["id", "access_level"]

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )