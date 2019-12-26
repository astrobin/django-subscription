from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = (
    url(r'^done/', TemplateView.as_view(template_name='subscription/subscription_done.html'), name='subscription_done'),
    url(r'^change-done/', TemplateView.as_view(template_name='subscription/subscription_change_done.html'),
        name='subscription_change_done'),
    url(r'^cancel/', TemplateView.as_view(template_name='subscription/subscription_cancel.html'),
        name='subscription_cancel'),
)

urlpatterns += (
    (r'^$', 'subscription_list', {}, 'subscription_list'),
    (r'^(?P<object_id>\d+)/$', 'subscription_detail', {}, 'subscription_detail'),
    (r'^(?P<object_id>\d+)/(?P<payment_method>(standard|pro))/$', 'subscription_detail', {}, 'subscription_detail'),
)

urlpatterns += (
    (r'^paypal/', include('paypal.standard.ipn.urls')),
)
