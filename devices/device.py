from devices.decorators import *
import datetime


class Device:
    def __init__(self, uid, d_type, d_version, manufacturer, production_date):
        self.__uid__ = uid
        self.set_device_type(d_type)
        self.set_device_version(d_version)
        self.set_manufacturer(manufacturer)
        self.set_date(production_date)

    @device_type
    def set_device_type(self, type):
        self.d_type = type

    @device_version
    def set_device_version(self, version):
        self.__d_version__ = version

    @manufacturer_name
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    @date_format(datetime.date(1990, 1, 1), datetime.date.today())
    def set_date(self, date):
        self.__production_date__ = date

    def print_info(self):
        print('UID: %s\n'
              'Device Type: %s\n'
              'Device Version: %s\n'
              'Manufacturer: %s\n'
              'Production Date: %s\n'
              % (self.__uid__,
                 self.d_type,
                 self.__d_version__,
                 self.manufacturer,
                 self.__production_date__))
