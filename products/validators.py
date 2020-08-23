from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# check that the rating value is less than 5
def validate_quantities_available(value):
    if value < 1:
        raise ValidationError(
            _("Sorry we're sold out! 😕"),
            params={'value': value},
        )