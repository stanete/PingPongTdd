from videoclub.flags.models import Flag


def is_active(flag_name):
    return Flag.objects.filter(name=flag_name, is_active=True).exists()
