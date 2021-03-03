from django.forms import ModelForm, MultipleChoiceField, CheckboxSelectMultiple
from .models import *


class AddEditWorkshopForm(ModelForm):
    # speakers = MultipleChoiceField(choices=Speaker.objects.all(), label='Orator',
    #                                widget=CheckboxSelectMultiple)
    class Meta:
        model = Workshop
        fields = ['codename', 'start_date', 'end_date',
                  'registration_start_date', 'registration_end_date',
                  'speakers', 'is_in_person', 'is_published']