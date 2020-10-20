from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import Palaute, Toimipiste
from django.utils.translation import gettext_lazy as _

GRADE_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'email', 'password1', 'password2'
            ]


class PalauteForm(ModelForm):
    arvosana = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

    class Meta:
        model = Palaute
        fields = [
            'FK_toimipiste_id', 'palaute_pvm',
            'arvosana', 'hyvaa', 'huonoa', 'parannettavaa'
            ]
        labels = {
            'FK_toimipiste_id': _('Valitse ravintola, josta annat palautetta.'),
            'hyvaa': _('Hyvää:')
        }
        widget = forms.CheckboxSelectMultiple,
        choices = GRADE_CHOICES
