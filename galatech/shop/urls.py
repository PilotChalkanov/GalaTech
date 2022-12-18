from django.urls import path

from galatech.shop.views import ProductListView
from galatech.web.views.about import AboutPageView
from galatech.web.views.contact import ContactMessageView
from galatech.web.views.vacation_requests import (
    EmployeeVacationRequestView,
    ListEmployeeVacationRequestView,
)
from galatech.web.views.generic import HomeView, DashboardView
from galatech.web.views.ticket import TicketCreateView, TicketListView

urlpatterns = [path("/products", ProductListView.as_view(), name="products")]
