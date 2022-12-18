from django import forms

from galatech.web.models import (
    Ticket,
    EmployeeVacationRequestModel,
    ContactMessageModel,
)


class TicketCreateForm(forms.ModelForm):

    """Ticket form for creating work related jobs"""

    class Meta:
        model = Ticket
        fields = "__all__"


class TicketEditForm:
    pass


class TicketDeleteForm:
    pass


class DateInput(forms.DateInput):
    input_type = "date"


class EmplotyeeVacationRequestForm(forms.ModelForm):
    """DaysOff request form"""

    class Meta:
        model = EmployeeVacationRequestModel
        exclude = ("user",)
        widgets = {
            "fromDate": DateInput(),
            "toDate": DateInput(),
        }


class ContactMessageForm(forms.ModelForm):
    """The contact form"""

    class Meta:
        model = ContactMessageModel
        fields = "__all__"
