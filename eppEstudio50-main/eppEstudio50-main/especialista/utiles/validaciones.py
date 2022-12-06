import re

from django.core.exceptions import ValidationError
from django.utils import timezone


def  validacion_ci(value):
    p = re.compile(u"[0-9]{11}$")
    m = p.match(value)
    if not m:
        raise ValidationError('CI incorrecto.')
    year, month, day = int(value[0:2]), int(value[2:4]), int(value[4:6])
    if month < 1 or month > 12 or day < 1 or \
            (month in [4, 6, 9, 11] and day > 30) or \
            (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or \
            (month == 2 and ((year % 4 == 0 and day > 29) or (year % 4 != 0 and day > 28))) or \
            (6 <= int(value[6]) <= 8 and year > timezone.now().year % 100):
        raise ValidationError('CI incorrecto.')