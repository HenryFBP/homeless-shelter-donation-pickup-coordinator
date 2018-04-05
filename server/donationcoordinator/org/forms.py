from django import forms
from django.forms import ModelForm

from .models import Org


class OrgForm(ModelForm):
    class Meta:
        model = Org
        exclude = ('location',)


class HomeSearchForm(forms.Form):
    """For searching a list of Homes."""
    class Meta:
        default_miles = 5

    miles = forms.IntegerField(initial=Meta.default_miles)
