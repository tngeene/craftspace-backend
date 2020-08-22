import json

from django.db import models

from orders.models import Order


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#  enables us to put common info into a number of other models i.e time
    class Meta:
        abstract = True

# does validation before accepting payments
class MpesaCalls(CommonInfo):
    ip_address = models.TextField()
    caller = models.TextField()
    conversion_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'


# stores accepted mpesa payments
class MpesaCallBacks(CommonInfo):
    ip_address = models.TextField()
    caller = models.TextField()
    conversion_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'

class PaymentManager(models.Manager):
    # saving the processed order payment to db
    def save_api_response(self, request, order=None):
        mpesa_body = request.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        payment = self.create(
            first_name = mpesa_payment['FirstName'],
            last_name=mpesa_payment['LastName'],
            middle_name=mpesa_payment['MiddleName'],
            description=mpesa_payment['TransID'],
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            organization_balance=mpesa_payment['OrgAccountBalance'],
            transaction_type=mpesa_payment['TransactionType'],
        )

        if order:
            payment.order = order
            payment.save()
            payment.refresh_from_db()
        return payment


#stores successful transactions
class MpesaPayment(CommonInfo):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    description = models.TextField()
    payment_type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    organization_balance = models.DecimalField(max_digits=10,decimal_places=2)

    objects = PaymentManager()

    def __str__(self):
        return f" {self.first_name} {self.amount}"
