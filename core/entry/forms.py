from django.forms import ModelForm
from .models import EntryRequest


class RequestForm(ModelForm):
    class Meta:
        model = EntryRequest
        fields = [
            'email'
        ]
