from client import Client
import uuid


class Bank:
    def __init__(self, bank_id, bank_name):
        self.__bank_id = bank_id
        self.__bank_name = bank_name
        self.__clients = {}
        self.__accounts = {}

    def get_name(self):
        return self.__bank_name

    def get_client(self, client_id):
        return self.__clients[client_id]

    def get_list_of_clients(self):
        return [{client_id, client.get_client_name()}
                for client_id, client in self.__clients.items()]

    def get_client_total_amount_of_money(self, client_id):
        return self.__clients[client_id].get_total_amount_of_mooney()

    def get_client_accounts(self, client_id):
        return self.__clients[client_id].get_accounts()

    def add_client(self, client_name):
        client_id = uuid.uuid4()
        client = Client(client_id, client_name)
        self.__clients[client_id] = client

    def remove_client(self, client_id):
        del self.__clients[client_id]

    def add_account(self, client_id, amount_of_mooney=0):
        account_id = uuid.uuid4()
        account = self.__clients[client_id].open_account(account_id, self.__bank_id, amount_of_mooney)
        self.__accounts[account_id] = account

    def get_list_of_accounts(self):
        return [{account_id, self.__clients[account.get_client_id()].get_client_name()}
                for account_id, account in self.__accounts.items()]

    def get_total_amount_of_mooney(self):
        return sum(account.get_amount_of_mooney() for account in self.__accounts.values())

