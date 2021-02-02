from django.forms import ModelForm
from .models import *


class AddEditWorkshopForm(ModelForm):
    class Meta:
        model = Workshop
        fields = ['code_name', 'start_date', 'end_date',
                  'registration_start_date', 'registration_end_date',
                  'speakers', 'is_in_person', 'is_published']

    # def __init__(self, *args, **kwargs):
    #     super(AddEditWorkshopForm, self).__init__(*args, **kwargs)
    #     for key in self.fields:
    #         self.fields[key].widget.attrs.update({
    #             'style': 'width:80%',
    #             'class': 'col-lg-10',
    #         })