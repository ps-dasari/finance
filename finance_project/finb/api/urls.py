from django.urls import path
from finb.api import views


urlpatterns = [
    path('company/', views.company_view),
    path('capi/', views.company_api),
    path('capi/<int:pk>', views.company_api_i),
    path('customer/', views.customer_api,name='customer')

]
