from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# check that the rating value is less than 5
def validate_rating(value):
    if value > 5:
        raise ValidationError(
            _('Rating should be less than or equal to 5'),
            params={'value': value},
        )