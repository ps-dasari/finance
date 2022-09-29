from django.urls import path
from finb.api import views


urlpatterns = [
    path('company/', views.company_view),
    path('companydata/', views.company_List),
    path('companydata/<int:pk>', views.company_Details),
    path('customerdata/', views.customer_List),
    path('customerdata/<int:pk>', views.customer_Detail),
    path('areasdata/', views.areas_List,name='areas'),
    path('areasdata/<int:pk>', views.area_Details),
    path('accounts/', views.accounts_List),
    path('accounts/<int:pk>', views.accounts_Detail)

]
