from django.urls import path
from galatech.web.views.about import AboutPageView
from galatech.web.views.generic import HomeView, DashboardView
from galatech.web.views.ticket import TicketCreateView, TicketListView

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/tickets", TicketListView.as_view(), name="tickets"),
    path("ticket/create", TicketCreateView.as_view(), name="ticket-create"),
    path("about/", AboutPageView.as_view(), name="about"),
]
