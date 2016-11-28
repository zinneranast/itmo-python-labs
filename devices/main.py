from devices.device import Device
from devices.exceptions import *
import csv


def csv_file_reader(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        return [row for row in reader]


def main():
    data = csv_file_reader('devices.csv')
    for device in data:
        try:
            device = Device(device[0], device[1], device[2], device[3], device[4])
            print('Device in csv format: \n' + device.csv + '\n')
            print('Device in xml format: \n' + device.xml + '\n')
            device.print_info()
        except InvalidDeviceTypeException as e:
            e.print_message()
        except InvalidDeviceVersionException as e:
            e.print_message()
        except InvalidManufacturerException as e:
            e.print_message()
        except InvalidDateException as e:
            e.print_message()


main()
