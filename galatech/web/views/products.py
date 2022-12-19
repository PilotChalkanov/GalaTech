from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from galatech.shop.models import Product
from galatech.web.forms import ProductCreateForm


class CreateProductView(LoginRequiredMixin, CreateView, ListView):
    form_class = ProductCreateForm
    context_object_name = "products"
    model = Product
    template_name = "products/create_product.html"
    success_url = reverse_lazy("create-product")



