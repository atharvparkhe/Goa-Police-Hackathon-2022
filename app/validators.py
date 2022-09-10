from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from os.path import splitext

VALID_EXTENSIONS = [".mp3", ".wav", ".aiff", ".flac", ".aac"]

MAX_SIZE = 25*1024*1024


def validate_file_extension(value):
    try:
        ext = splitext(value.name)[1].lower()
        if ext not in VALID_EXTENSIONS:
            raise ValidationError(
            _('%(value)s is an invalid file type'),
            params={'value': value},
            )
        return value
    except:
        raise ValidationError(
            _('%(value)s is an invalid file type'),
            params={'value': value},
        )



def validate_file_size(value):
    try:
        filesize = len(value)
        if filesize > MAX_SIZE:
            raise ValidationError(
                _('%(value)s file is loo large'),
                params={'value': value},
            )
    except:
        raise ValidationError(
            _('%(value)s file is loo large'),
            params={'value': value},
        )

