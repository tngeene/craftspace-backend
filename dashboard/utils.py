from django.http import request
from django.utils.crypto import get_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def send_welcome_email(user, password,request):
    current_site = get_current_site(request)
    subject = 'TuK Account activation'
    message = render_to_string('account/password_reset_email.html', {
        'user': user.first_name,
        'email': user.email,
        'domain': current_site.domain,
        'password': password,
        })
    email = EmailMultiAlternatives(
    subject, message, from_email='tuklabs@tuk.ac.ke', to=[user.email, ])
    email.content_subtype = 'html'
    email.send()


def send_suspension_email(user, request):
    current_site = get_current_site(request)
    subject = 'Craftspace Account Suspension'
    message = render_to_string('account/email/account_deactivated.html', {
        'user': user.first_name,
        'domain': current_site.domain,
        'site_name': current_site.name,
        })
    email = EmailMultiAlternatives(
    subject, message, from_email='admin@craftspace.com', to=[user.email, ])
    email.content_subtype = 'html'
    email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    subject = 'Craftspace Account Activation'
    message = render_to_string('account/email/account_reactivated.html', {
        'user': user.first_name,
        'domain': current_site.domain,
        'site_name': current_site.name,
        })
    email = EmailMultiAlternatives(
    subject, message, from_email='admin@craftspace.com', to=[user.email, ])
    email.content_subtype = 'html'
    email.send()