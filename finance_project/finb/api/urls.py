from django.urls import path
from finb.api import views


urlpatterns = [
    path('cname/', views.company_view),

]
