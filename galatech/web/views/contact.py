from django.urls import reverse_lazy
from django.views.generic import CreateView

from galatech.web.forms import ContactMessageForm
from galatech.web.models import ContactMessageModel


class ContactMessageView(CreateView):

    model = ContactMessageModel
    form_class = ContactMessageForm
    template_name = "web/contact.html"
    success_url = reverse_lazy("about")
