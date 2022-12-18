from django.urls import path
from galatech.auth_app.views.auth_views import (UserLoginView,
                                                UserRegisterView,
                                                CreateProfileView,
                                                UserLogoutView,
                                                FarewellView,
                                                ChangeUserPasswordView,
                                                UserPasswordResetView,
                                                SuccessPassChangeView
                                                )

from galatech.auth_app.views.products import CreateProductView

urlpatterns = (
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", CreateProfileView.as_view(), name="profile"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("farewell/", FarewellView.as_view(), name="farewell"),
    path("password_change/", ChangeUserPasswordView.as_view(), name="password_change"),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path("success/", SuccessPassChangeView.as_view(), name="success-url"),
    path("create_product/", CreateProductView.as_view(), name="create_product"),
)
