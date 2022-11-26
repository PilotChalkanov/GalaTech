from django.contrib.auth import views as auth_views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.views.generic import FormView

from galatech.auth_app.forms import UserRegistrationForm, ProfileCreationForm, UserModel
from galatech.auth_app.models import GalaTechUser, GalaTechProfile


class UserRegisterView(generic_views.CreateView):
    """The registration logic for the user registration"""
    form_class = UserRegistrationForm
    template_name = 'auth_app/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class UserLoginView(auth_views.LoginView):
    """The login logic for the user login"""

    template_name = 'auth_app/login.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class ProfileCreateView(generic_views.CreateView):
    """The profile creation for the user registration"""

    form_class = ProfileCreationForm
    template_name = 'auth_app/profile.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def post(self, request, *args, **kwargs):
        self.object = UserModel.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

class UserLogoutView(auth_views.LogoutView):
    """The login logic for the user login"""
    pass

class FarewellView(auth_views.TemplateView):
    """The login logic for the user login"""
    template_name = 'auth_app/logout.html'



class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'auth_app/profile.html'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('profile')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = GalaTechProfile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = GalaTechProfile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['photo']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object


class EditProfileView:
    pass

class ChangeUserPasswordView:
    pass




