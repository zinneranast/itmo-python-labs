class InvalidDeviceTypeException(Exception):
    def print_message(self):
        print("ERROR: Invalid device type\n")


class InvalidDeviceVersionException(Exception):
    def print_message(self):
        print("ERROR: Invalid device version\n")


class InvalidManufacturerException(Exception):
    def print_message(self):
        print("ERROR: Invalid manufacturer name\n")


class InvalidDateException(Exception):
    def print_message(self):
        print("ERROR: Invalid date\n")