from django.urls import path

from galatech.auth_app.views import UserLoginView, DashboardView, TicketCreateView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('ticket/create', TicketCreateView.as_view(), name='ticket-create'),

)