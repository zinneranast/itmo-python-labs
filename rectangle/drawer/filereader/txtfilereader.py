def read(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        raise FileNotFoundError
    except Exception:
        raise Exception
