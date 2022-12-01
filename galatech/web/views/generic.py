from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic as views
from django.views.generic import ListView

from galatech.auth_app.models import GalaTechProfile
from galatech.web.models import Ticket


class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin,ListView):
    model = Ticket
    template_name = 'base/dashboard.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        user_profile= GalaTechProfile.objects.get(pk=user.id)
        context['user_profile_photo'] = user_profile.photo.url
        return context
