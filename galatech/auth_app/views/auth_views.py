from django.contrib import messages
from django.contrib.auth import views as auth_views, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.views.generic import UpdateView
from galatech.auth_app.forms import (
    UserRegistrationForm,
    ProfileCreationForm,
    ChangeUserPasswordForm,
    UserPasswordResetForm, ProfileEditForm,
)
from galatech.auth_app.models import GalaTechProfile

UserModel = get_user_model()


class UserRegisterView(generic_views.CreateView):
    """The registration logic for the user registration"""

    form_class = UserRegistrationForm
    model = UserModel
    template_name = "auth_app/register.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        if form.cleaned_data.get("staff_id") is not None:
            form.instance.is_staff = True
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    """The login logic for the user login"""

    template_name = "auth_app/login.html"
    success_url = reverse_lazy("dashboard")

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class CreateProfileView(generic_views.CreateView):
    """The profile creation logic for the user registration"""

    template_name = "auth_app/profile.html"
    success_url = reverse_lazy("dashboard")
    form_class = ProfileCreationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserLogoutView(auth_views.LogoutView):
    """The login logic for the user login"""

    pass


class FarewellView(auth_views.TemplateView):
    """The login logic for the user login"""

    template_name = "auth_app/logout.html"

@login_required
def update_profile(request, pk):
    profile = GalaTechProfile.objects.get(user_id=pk)
    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, request.FILES,instance=profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='dashboard')

    profile_form = ProfileEditForm(instance=profile)

    return render(request, 'auth_app/profile_edit.html', {'form': profile_form})

class ChangeUserPasswordView(PasswordChangeView):
    template_name = "auth_app/change_user_password.html"
    form_class = ChangeUserPasswordForm
    success_url = reverse_lazy("success-url")

    def get_success_url(self):
        if self.success_url:
            logout(self.request)
            return self.success_url
        return super().get_success_url()


class SuccessPassChangeView(auth_views.TemplateView):
    template_name = "auth_app/success.html"


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = "auth_app/password_reset.html"
