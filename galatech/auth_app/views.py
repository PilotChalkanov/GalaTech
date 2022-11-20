from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from galatech.auth_app.models import Ticket


class UserRegisterView:
    pass

class UserLoginView(auth_views.LoginView):
    template_name = 'auth_app/login.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class UserDetailsView:
    pass

class EditProfileView:
    pass

class ChangeUserPasswordView:
    pass


class DashboardView(LoginRequiredMixin,ListView):
    model = Ticket
    template_name = 'auth_app/dashboard.html'

class TicketCreateView(LoginRequiredMixin, CreateView):

    model = Ticket
    template_name = 'auth_app/ticket_create.html'

    success_url = reverse_lazy('dashboard')
    fields = ('title', 'type', 'status', 'photo', 'description')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
