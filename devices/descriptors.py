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
    def __init__(self, list):
        self.list = list

    def __get__(self, obj, objtype=None):
        result = '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE ' + type(obj).__name__ + '>\n'
        for attr in self.list:
            result += '\t<' + attr + '>\n\t\t' + getattr(obj, attr) + '\n\t</' + attr + '>\n'
        result += '</' + type(obj).__name__ + '>'

        if result.endswith(','):
            result = result[:-1]

        return result
