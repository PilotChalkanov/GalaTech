from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from galatech.web.forms import EmplotyeeVacationRequestForm
from galatech.web.models import EmployeeVacationRequestModel


class EmployeeVacationRequestView(LoginRequiredMixin, CreateView):
    model = EmployeeVacationRequestModel
    form_class = EmplotyeeVacationRequestForm
    template_name = "web/days_off_req.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        day_off_req = form.save(commit=False)
        day_off_req.user = self.request.user
        day_off_req.save()
        return super().form_valid(form)


class ListEmployeeVacationRequestView(LoginRequiredMixin, ListView):

    template_name = "web/day_off_req_table.html"
    context_object_name = "requests_"
    model = EmployeeVacationRequestModel

    def post(self, request, *args, **kwargs):
        input_request_id = request.POST.getlist("approvedRequests")
        req_to_approve = EmployeeVacationRequestModel.objects.filter(
            id__in=input_request_id
        )
        if req_to_approve:
            req_to_approve.update(is_approved=True)
            return redirect("list-days-off-req")
        return redirect("list-days-off-req")
