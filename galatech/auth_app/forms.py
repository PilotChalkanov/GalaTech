from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from galatech.auth_app.models import GalaTechProfile


class UserRegistrationForm(auth_forms.UserCreationForm):
    """A form for creating new users."""

    class Meta:
        model = get_user_model()
        fields = ("email", "staff_id")

    error_messages = {"password_mismatch": "The two password didn't match."}


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = GalaTechProfile
        exclude = ("user",)
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter last name",
                }
            ),
            "age": forms.TextInput(
                attrs={
                    "placeholder": "Age",
                }
            ),
            "Address": forms.TextInput(
                attrs={
                    "placeholder": "Enter your address",
                }
            ),
        }

class ChangeUserPasswordForm(auth_forms.PasswordChangeForm):
    """A form for changing user's password."""

    class Meta:
        model = get_user_model()
        widgets = {
            "old_password": forms.PasswordInput(
                attrs={
                    "placeholder": "Enter your old password",
                }
            ),
            "last_name": forms.PasswordInput(
                attrs={
                    "placeholder": "Enter new password",
                }
            ),
            "age": forms.PasswordInput(
                attrs={
                    "placeholder": "Confirm password",
                }
            )
        }

class UserPasswordResetForm(auth_forms.PasswordResetForm):
    class Meta:
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email",
                },)
        }
