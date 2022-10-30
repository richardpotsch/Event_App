from django.core.exceptions import ValidationError
from django.forms import ModelForm

from base.models import Event, Type_event


class EventForm(ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 4:
            validation_error = ValidationError("Jméno je moc krátké.")
            raise validation_error
        return name

    class Meta:
        model = Event
        fields = '__all__'
        #exclude = [''] # fields you want to exclude from form as list

