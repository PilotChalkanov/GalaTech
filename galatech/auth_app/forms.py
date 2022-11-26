from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from galatech.auth_app.models import GalaTechProfile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):

    """  A form for creating new users.  """
    class Meta:
        model = UserModel
        fields = ('email','password1','password2')

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = GalaTechProfile
        exclude = ('user',)
