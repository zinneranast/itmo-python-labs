from banks.client import Client
from banks.transaction import MonetaryTransaction
from datetime import datetime
import uuid


class Bank:
    def __init__(self, bank_id, bank_name):
        self.__bank_id = bank_id
        self.__bank_name = bank_name
        self.__clients = {}
        self.__accounts = {}
        self.__transactions = {}

    def get_name(self):
        return self.__bank_name

    def get_bank_id(self):
        return self.__bank_id

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

    def occur_bank_ransfer(self, sending_account_id, receiving_account_id,
                           amount_of_payment, sending_bank_id='', receiving_bank_id='', monetary='RUB',
                           exchange_rate=''):
        if monetary != 'RUB':
            self.__check_transaction(sending_account_id, receiving_account_id,
                                     amount_of_payment, sending_bank_id, receiving_bank_id, monetary,
                                     exchange_rate)
        else:
            if sending_bank_id == '':
                sending_bank_id = self.__bank_id
            if receiving_bank_id == '':
                receiving_bank_id = self.__bank_id
            self.__accounts[sending_account_id].withdraw_money(receiving_bank_id, amount_of_payment, monetary,
                                                               exchange_rate)
            self.__accounts[receiving_account_id].deposit_mooney(sending_bank_id, amount_of_payment, monetary,
                                                                 exchange_rate)

    def __check_transaction(self, sending_account_id, receiving_account_id,
                            amount_of_payment, sending_bank_id, receiving_bank_id, monetary,
                            exchange_rate):
        date_of_payment = datetime.date()
        transaction = MonetaryTransaction(sending_bank_id, receiving_bank_id, amount_of_payment,
                                          date_of_payment,
                                          monetary.Monetary[monetary], exchange_rate)
        transaction_id = uuid.uuid4()
        self.__transactions[transaction_id] = (transaction, sending_account_id, receiving_account_id)

    def bank_decision(self, transaction_id, decision):
        if decision == True:
            transaction, sending_account_id, receiving_account_id = self.__transactions[transaction_id]
            sending_bank_id = transaction.get_sending_bank()
            receiving_bank_id = transaction.get_receiving_bank()
            amount_of_payment = transaction.get_amount_of_payment_in_rubles()
            monetary = transaction.get_monetary_id()
            exchange_rate = transaction.get_exchange_rate()
            self.occur_bank_transfer(sending_account_id, receiving_account_id,
                                    amount_of_payment, sending_bank_id, receiving_bank_id, monetary,
                                    exchange_rate)
        else:
            del self.__transactions[transaction_id]
