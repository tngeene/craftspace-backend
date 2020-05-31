import requests
from  datetime import datetime
from requests.auth import HTTPBasicAuth
import json
from base64 import b64encode

consumer_key = "YjA61YtxaMTPhVldfG0OpfZRCEiwPxXU"
consumer_secret = "LpSZu8LmE8BmUGu1"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
Passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
Shortcode = 174379


def get_token():
  r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
  token = r.json()
  return(token["access_token"])
token = get_token()


def get_time():
  now = str(datetime.now().strftime("%Y%m%d"))
  time = str(datetime.now().strftime("%H%M%S"))
  real = str(now+time)
  return real

githaa = get_time()
short = str(Shortcode)

def encoded_pass():
  pwd = (short+Passkey+githaa).encode('utf-8')
  pwd_enc = b64encode(pwd).decode('ascii')
  return pwd_enc

pass_enc = encoded_pass()


access_token = token
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
  "BusinessShortCode": Shortcode,
  "Password": pass_enc,
  "Timestamp": githaa,
  "TransactionType": "CustomerPayBillOnline",
  "Amount": 1,
  "PartyA": "254708651848",
  "PartyB":  Shortcode,
  "PhoneNumber": "254708651848",
  "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
  "AccountReference": "6579",
  "TransactionDesc": " paying school fees"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)