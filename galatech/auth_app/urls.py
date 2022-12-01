from django.urls import path
from galatech.auth_app.views import UserLoginView, UserRegisterView, UserLogoutView, FarewellView, CreateProfileView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', CreateProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('farewell/', FarewellView.as_view(), name='farewell'),
)