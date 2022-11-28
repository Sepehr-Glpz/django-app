import django.forms as forms
from .models import ManagementUser


class DisplayForm(forms.ModelForm):
    def __init__(self, access_level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = set_field_lock(access_level, "username")
        self.fields["name"].disabled = set_field_lock(access_level, "name")
        self.fields["email"].disabled = set_field_lock(access_level, "email")
        self.fields["national_code"].disabled = set_field_lock(access_level, "national_code")
        self.fields["birth_date"].disabled = set_field_lock(access_level, "birth_date")
        self.fields["salary"].disabled = set_field_lock(access_level, "salary")

    class Meta:
        model = ManagementUser
        fields = [
            "username",
            "name",
            "email",
            "national_code",
            "birth_date",
            "salary",
        ]


fields_access = {
    "username": {2, 3},
    "name": {2, 3},
    "email": {2, 3},
    "national_code": {2, 3},
    "birth_date": {2, 3},
    "salary": {3},
}


def set_field_lock(user_level, field_name):
    if user_level in fields_access[field_name]:
        return False
    else:
        return True
