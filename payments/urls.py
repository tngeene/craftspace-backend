from django.urls import path
from payments.views import getAccessToken, lipa_na_mpesa_online, register_urls, \
    validation, call_back, confirmation

app_name = "payments"

urlpatterns = [
    path('access/token',getAccessToken,name='get_mpesa_access_token'),
    path('online/lipa',lipa_na_mpesa_online,name='lipa_na_mpesa'),

    # register, confirmation, validation and callback urls
    path('c2b/register',register_urls,name='register_mpesa_validation'),
    path('c2b/confirmation',confirmation,name='confirm_payments'),
    path('c2b/validation',validation,name='validate_payments'),
    path('c2b/callback',call_back,name='mpesa_call_back'),
]
