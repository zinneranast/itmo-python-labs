from devices.decorators import *
from devices.descriptors import *


class Device(object):
    csv = CsvDescriptor(['uid', 'type', 'version', 'manufacturer', 'production_date'])
    xml = XmlDescriptor(['uid', 'type', 'version', 'manufacturer', 'production_date'])

    def __init__(self, uid, type, version, manufacturer, production_date):
        self.uid = uid
        self.set_device_type(type)
        self.set_device_version(version)
        self.set_manufacturer(manufacturer)
        self.set_date(production_date)

    @device_type
    def set_device_type(self, type):
        self.type = type

    @device_version
    def set_device_version(self, version):
        self.version = version

    @manufacturer_name
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    @date_format
    def set_date(self, date):
        self.production_date = date

    def print_info(self):
        print('UID: %s\n'
              'Device Type: %s\n'
              'Device Version: %s\n'
              'Manufacturer: %s\n'
              'Production Date: %s\n'
              % (self.uid,
                 self.type,
                 self.version,
                 self.manufacturer,
                 self.production_date))
