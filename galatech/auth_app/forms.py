from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from galatech.auth_app.models import GalaTechProfile, GalaTechUser


class UserRegistrationForm(auth_forms.UserCreationForm):

    """  A form for creating new users.  """
    class Meta:
        model = get_user_model()
        fields = ('email', 'staff_id')

    error_messages = {
        'password_mismatch': "The two password didn't match."
    }

class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = GalaTechProfile
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),
            'Address': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your address',
                }
            )
        }








