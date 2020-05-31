import requests
import json
from requests.auth import HTTPBasicAuth
from  datetime import datetime
from base64 import b64encode, encode
from decouple import config


class MpesaC2bCredentials:
    consumer_key = config('CONSUMER_KEY')
    consumer_secret = config('CONSUMER_SECRET')
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredentials.api_URL,
        auth=HTTPBasicAuth(MpesaC2bCredentials.consumer_key,
            MpesaC2bCredentials.consumer_secret))
    mpesa_access_token = r.json()
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipaNaMpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    business_shortcode = config('BS_SHRT_CODE')
    passkey = config('MPESA_PASSKEY')
    test_c2b_shortcode = config('TEST_C2B_SHORT_CODE')
    data_to_encode = business_shortcode + passkey + lipa_time

    online_password = b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')