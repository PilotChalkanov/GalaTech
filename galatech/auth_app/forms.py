import os
from os.path import join

from django import forms
from django.conf import settings
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.exceptions import ValidationError

from galatech.auth_app.models import GalaTechProfile
from galatech.shop.models import Product


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


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = GalaTechProfile
        exclude = ('user',)

    def save(self, commit=True):
        db_profile = GalaTechProfile.objects.get(pk=self.instance.user_id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_profile.photo))
            os.remove(image_path)
        return super().save(commit)


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
            ),
        }


class UserPasswordResetForm(auth_forms.PasswordResetForm):
    class Meta:
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email",
                },
            )
        }

