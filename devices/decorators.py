from devices.exceptions import *
from functools import wraps
import datetime
import re


def device_type(device_types):
    def decorator(set_device_type):
        @wraps(set_device_type)
        def wrapper(self, type):
            if type in device_types:
                return set_device_type(self, type)
            else:
                raise InvalidDeviceTypeException

        return wrapper

    return decorator


def device_version(regex):
    def decorator(set_device_version):
        @wraps(set_device_version)
        def wrapper(self, version):
            if not re.match(regex, version):
                raise InvalidDeviceVersionException
            return set_device_version(self, version)

        return wrapper

    return decorator


def manufacturer_name(max):
    def decorator(set_manufacturer):
        @wraps(set_manufacturer)
        def wrapper(self, manufacturer):
            if len(manufacturer) < 1 or len(manufacturer) > max:
                raise InvalidManufacturerException
            return set_manufacturer(self, manufacturer)

        return wrapper

    return decorator


def date_format(min, max):
    def parse_date(date):
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            if date < min or date > max:
                return False
        except:
            return False
        return True

    def decorator(set_date):
        @wraps(set_date)
        def wrapper(self, date):
            if parse_date(date):
                return set_date(self, date)
            else:
                raise InvalidDateException

        return wrapper

    return decorator
