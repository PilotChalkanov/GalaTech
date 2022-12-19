from django.urls import path
from galatech.auth_app.views.auth_views import (
    UserLoginView,
    UserRegisterView,
    CreateProfileView,
    UserLogoutView,
    FarewellView,
    ChangeUserPasswordView,
    UserPasswordResetView,
    SuccessPassChangeView, update_profile, DeleteProfileView, UserLogoutConfirmationView,
)

from galatech.web.views.products import CreateProductView

urlpatterns = (
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", CreateProfileView.as_view(), name="profile"),
    path("profile/edit/<int:pk>", update_profile, name="profile-edit"),
    path("profile/delete/<int:pk>", DeleteProfileView.as_view(), name="delete-profile"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("logout/confirmation", UserLogoutConfirmationView.as_view(), name="logout-confirm"),
    path("farewell/", FarewellView.as_view(), name="farewell"),
    path("password_change/", ChangeUserPasswordView.as_view(), name="password_change"),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path("success/", SuccessPassChangeView.as_view(), name="success-url")

)
