from django.urls import path, include
from .views import PrinterHomePageView, AboutPageView, ServicePageView, ContactsPageView, PrinterCreateView

urlpatterns = [
    path('',PrinterHomePageView.as_view(), name='printer-home'),
    path('about/',AboutPageView.as_view(), name='pabout'),
    path('services/',ServicePageView.as_view(), name='pservices'),
    path('contacts/', ContactsPageView.as_view(), name='pcontact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('print/new/', PrinterCreateView.as_view(), name='print_new'),
]