# djauth/urls.py
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic.base import TemplateView

urlpatterns = [
    url('', TemplateView.as_view(template_name='home.html'), name='home'),
    url('admin/', admin.site.urls),
    url('accounts/', include('accounts.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
]