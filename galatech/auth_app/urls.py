from django.urls import path

from galatech.auth_app.views import (
    UserLoginView,
    UserRegisterView,
    UserLogoutView,
    FarewellView,
    CreateProfileView, ChangeUserPasswordView, SuccessPassChangeView, UserPasswordResetView,
)

urlpatterns = (
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", CreateProfileView.as_view(), name="profile"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("farewell/", FarewellView.as_view(), name="farewell"),
    path("password_change/", ChangeUserPasswordView.as_view(), name="password_change"),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path("success/", SuccessPassChangeView.as_view(), name="success-url")
)
