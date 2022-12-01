from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.views.generic import FormView
from galatech.auth_app.forms import UserRegistrationForm, ProfileCreationForm
from galatech.auth_app.models import GalaTechProfile, GalaTechUser

UserModel = get_user_model()


class UserRegisterView(generic_views.CreateView):
    """The registration logic for the user registration"""
    form_class = UserRegistrationForm
    model = UserModel
    template_name = 'auth_app/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        if form.cleaned_data.get('staff_id') is not None:
            form.instance.is_staff = True
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    """The login logic for the user login"""
    template_name = 'auth_app/login.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class CreateProfileView(generic_views.CreateView):
    """The profile creation logic for the user registration"""
    template_name = 'auth_app/profile.html'
    success_url = reverse_lazy('dashboard')
    form_class = ProfileCreationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserLogoutView(auth_views.LogoutView):
    """The login logic for the user login"""
    pass


class FarewellView(auth_views.TemplateView):
    """The login logic for the user login"""
    template_name = 'auth_app/logout.html'


class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'auth_app/profile_edit.html'
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
