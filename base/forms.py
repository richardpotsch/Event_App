from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateTimeInput

from base.models import Event, Type_event, Message


class EventForm(ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 4:
            raise ValidationError("Jméno je moc krátké.")
        return name



    class Meta:
        model = Event
        fields = '__all__'
        #exclude = [''] # fields you want to exclude from form as list
        widgets = {
            'date_from': DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        #exclude = [''] # fields you want to exclude from form as list




