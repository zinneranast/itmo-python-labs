class Client:
    def __init__(self, client_id, client_name):
        self.__client_id = client_id
        self.__client_name = client_name

    def get_client_id(self):
        return self.__client_id

    def get_client_name(self):
        return self.__client_name