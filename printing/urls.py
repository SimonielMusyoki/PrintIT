from django.urls import path, include
from .views import HomePageView,AboutPageView, ServicePageView, ContactsPageView, PrintCreateView2, ViewPrinters, PrintCreateView
urlpatterns = [
    path('home/',HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),
    path('services/',ServicePageView.as_view(), name='services'),
    path('contacts/', ContactsPageView.as_view(), name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('print/new/', PrintCreateView.as_view(), name='print_new'),
    path('view/', ViewPrinters.as_view(), name='printer-view'),
    path('', PrintCreateView2.as_view(), name='print'),
]