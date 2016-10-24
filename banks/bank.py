from banks.client import Client
from banks.account import BankAccount
from banks.transaction import Transaction, MonetaryTransaction
from datetime import datetime
import uuid


class Bank:
    def __init__(self):
        self.__accounts = {}
        self.__transactions = {}
        self.__clients = {}

    def get_accounts(self):
        return self.__accounts.values()

    def get_clients(self):
        return self.__clients.values()

    def get_total_amount_of_mooney(self):
        return sum(account.get_amount_of_mooney() for account in self.__accounts.values())

    def get_amount_of_mooney_by_account_id(self, account_id):
        return self.__accounts[account_id].get_amount_of_mooney()

    def get_amount_of_mooney_by_client_id(self, client_id):
        amount_of_mooney = 0
        for account in self.__accounts.values():
            client_id_ = account.get_client_id()
            if client_id_ == client_id:
                amount_of_mooney += account.get_amount_of_mooney()

        return amount_of_mooney

    def get_transaction_history_by_account_id(self, account_id):
        transactions = []
        for transaction in self.__transactions:
            if transaction.get_sending_account_id() == account_id or transaction.get_receiving_account_id() == account_id:
                transactions.append(transaction)

        return transactions

    def add_client(self, client_name):
        client = Client(uuid.uuid4(), client_name)
        self.__clients[client.get_client_id()] = client

    def open_account(self, client_id, amount_of_mooney=0):
        account = BankAccount(uuid.uuid4(), self.__clients[client_id], amount_of_mooney)
        self.__accounts[account.get_account_id()] = account
        return account.get_account_id()

    def occur_bank_ransfer(self, sending_account_id,
                           receiving_account_id,
                           amount_of_payment,
                           monetary='RUB',
                           exchange_rate=''):

        if monetary != 'RUB':
            transaction = MonetaryTransaction(uuid.uuid4(),
                                              sending_account_id,
                                              receiving_account_id,
                                              amount_of_payment,
                                              datetime.date(),
                                              monetary,
                                              exchange_rate)
        else:
            transaction = Transaction(uuid.uuid4(),
                                      sending_account_id,
                                      receiving_account_id,
                                      amount_of_payment,
                                      datetime.date())

            self.__accounts[sending_account_id].withdraw_money(amount_of_payment)
            self.__accounts[receiving_account_id].deposit_mooney(amount_of_payment)

        self.__transactions[transaction.get_transaction_id()] = transaction

    def bank_decision(self, transaction_id, decision):
        if decision == True:
            transaction = self.__transactions[transaction_id]

            sending_account_id = transaction.get_sending_account_id()
            receiving_account_id = transaction.get_receiving_account_id()
            amount_of_payment = transaction.get_amount_of_payment_in_rubles()

            self.__accounts[sending_account_id].withdraw_money(amount_of_payment)
            self.__accounts[receiving_account_id].deposit_mooney(amount_of_payment)

        else:
            del self.__transactions[transaction_id]
