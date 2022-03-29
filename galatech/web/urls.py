from django.urls import path


from galatech.web.views import show_about, show_contacts, show_partners, show_services, show_tuning, \
    show_products, show_product_details, contact_us, IndexTemplateView

urlpatterns = (
    path('',IndexTemplateView.as_view(), name='show-index'),
    path('about/', show_about, name='show-about'),
    path('contacts/', show_contacts, name='show-contacts'),
    path('partners/', show_partners, name='show-partners'),
    path('services/', show_services, name='show-services'),
    path('tuning/', show_tuning, name='show-tuning'),
    path('products/', show_products, name='show-products'),
    path('pruduct_details/<int:id>', show_product_details, name='show-product-details'),
    path('contact_us/', contact_us, name='contact-us'),
)