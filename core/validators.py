from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date

today = date.today()
#check that the entered date is not in the past
def validate_date(value):
    if not value:
        if value < today:
            raise ValidationError(
                _("Date cannot be in the past, please enter a valid date."),
                params={'value': value},
            )