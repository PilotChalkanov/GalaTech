from django.urls import path
from galatech.web.views.about import AboutPageView
from galatech.web.views.contact import ContactMessageView
from galatech.web.views.products import CreateProductView
from galatech.web.views.vacation_requests import (
    EmployeeVacationRequestView,
    ListEmployeeVacationRequestView,
)
from galatech.web.views.generic import HomeView, DashboardView
from galatech.web.views.ticket import TicketCreateView, TicketListView

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/tickets", TicketListView.as_view(), name="tickets"),
    path("ticket/create", TicketCreateView.as_view(), name="ticket-create"),
    path("about/", AboutPageView.as_view(), name="about"),
    path(
        "dashboard/days_off", EmployeeVacationRequestView.as_view(), name="days-off-req"
    ),
    path("contact/", ContactMessageView.as_view(), name="contact"),
    path(
        "dashboard/approval_list",
        ListEmployeeVacationRequestView.as_view(),
        name="list-days-off-req",
    ),
    path("create_product/", CreateProductView.as_view(), name="create-product"),
]
