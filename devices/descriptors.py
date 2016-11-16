class CsvDescriptor(object):
    def __init__(self, list):
        self.list = list

    def __get__(self, obj, objtype=None):
        result = ""
        for attr in self.list:
            result += getattr(obj, attr) + ','

        if result.endswith(','):
            result = result[:-1]

        return result


class XmlDescriptor(object):
    def __get__(self, obj, objtype=None):
        uid = getattr(obj, '__uid__')
        d_type = getattr(obj, '__d_type__')
        d_version = getattr(obj, '__d_version__')
        manufacturer = getattr(obj, '__manufacturer__')
        production_date = getattr(obj, '__production_date__')

        result = '<?xml version="1.0" encoding="utf-8"?>\n' \
                 + '<!DOCTYPE device>\n\t' \
                 + '<device uid="' + uid + '">\n\t\t' \
                 + '<type>\n\t\t\t' + d_type + '\n\t\t</type>\n\t\t' \
                 + '<version>\n\t\t\t' + d_version + '\n\t\t</version>\n\t\t' \
                 + '<manufacturer>\n\t\t\t' + manufacturer + '\n\t\t</manufacturer>\n\t\t' \
                 + '<production>\n\t\t\t' + production_date + '\n\t\t</production>\n\t' \
                 + '</device>'

        return result
