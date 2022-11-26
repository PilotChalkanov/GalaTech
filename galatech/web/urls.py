from django.conf import settings
from django.conf.urls.static import static
from galatech.web.views.ticket import TicketCreateView, DashboardView
from django.urls import path, include

from galatech.web.views.generic import HomeView

urlpatterns = [

    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('ticket/create', TicketCreateView.as_view(), name='ticket-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)