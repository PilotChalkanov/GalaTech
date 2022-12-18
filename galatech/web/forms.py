from django import forms

from galatech.web.models import Ticket, DayOffRequestModel, ContactMessageModel


class TicketCreateForm(forms.ModelForm):

    """Ticket form for creating work related jobs"""

    class Meta:
        model = Ticket
        fields = ('__all__')


class TicketEditForm:
    pass


class TicketDeleteForm:
    pass


class DateInput(forms.DateInput):
    input_type = 'date'

class DaysOffRequestForm(forms.ModelForm):
    """DaysOff request form"""

    class Meta:
        model = DayOffRequestModel
        exclude = ('user',)
        widgets = {
            'fromDate': DateInput(),
            'toDate': DateInput(),
        }


class ContactMessageForm(forms.ModelForm):
    """The contact form"""

    class Meta:
        model = ContactMessageModel
        fields = ('__all__')