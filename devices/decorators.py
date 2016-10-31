from devices.exceptions import *
import datetime
import re

device_types = {
    'desktop': 'Desktop device description',
    'tablet': 'Tablet device description',
    'mobile': 'Mobile device description',
    'tv': 'TV device description'
}


def device_type(set_device_type):
    def wrapper(self, type):
        if type in device_types:
            return set_device_type(self, type)
        else:
            raise InvalidDeviceTypeException

    return wrapper


def device_version(set_device_version):
    def wrapper(self, version):
        if not re.match('[a-zA-Z]*[\-\.]*[0-9]+', version):
            raise InvalidDeviceVersionException
        return set_device_version(self, version)

    return wrapper


def manufacturer_name(set_manufacturer):
    def wrapper(self, manufacturer):
        if len(manufacturer) < 1 or len(manufacturer) > 30:
            raise InvalidManufacturerException
        return set_manufacturer(self, manufacturer)

    return wrapper


def date_format(set_date):
    def parse_date(date):
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            if date < datetime.date(1990, 1, 1) or date > datetime.date.today():
                return False
        except:
            return False
        return True

    def wrapper(self, date):
        if parse_date(date):
            return set_date(self, date)
        else:
            raise InvalidDateException

    return wrapper
