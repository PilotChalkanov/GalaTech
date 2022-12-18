from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from galatech.auth_app.forms import ProductCreateForm


class CreateProductView(LoginRequiredMixin, CreateView):
    form_class = ProductCreateForm
    template_name = "products/create_product.html"
    success_url = reverse_lazy("dashboard")