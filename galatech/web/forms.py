from django import forms

from galatech.web.models import Ticket


class TicketCreateForm(forms.ModelForm):

    """Ticket form for creating work related jobs"""

    class Meta:
        model = Ticket
        fields = "__all__"


class TicketEditForm:
    pass


class TicketDeleteForm:
    pass
