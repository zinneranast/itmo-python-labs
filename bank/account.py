from transaction import Transaction, MonetaryTransaction
import monetary
from datetime import datetime


class BankAccount:
    def __init__(self, account_id, bank_id, client_id, amount_of_mooney=0):
        self.__account_id = account_id
        self.__bank_id = bank_id
        self.__client_id = client_id
        self.__amount_of_mooney = amount_of_mooney
        self.__transaction_history = []

    def get_client_id(self):
        return self.__client_id

    def get_amount_of_mooney(self):
        return self.__amount_of_mooney

    def get_transaction_history(self):
        return self.__transaction_history

    def deposit_mooney(self, bank_id, amount_of_mooney, monetary='RUB', exchange_rate=''):
        self.__amount_of_mooney += amount_of_mooney
        date_of_payment = datetime.date()
        if monetary == 'RUB':
            transaction = Transaction(bank_id, self.__bank_id, self.__amount_of_payment, date_of_payment)
        else:
            transaction = MonetaryTransaction(bank_id, self.__bank_id, self.__amount_of_payment, date_of_payment,
                                              monetary.Monetary[monetary], exchange_rate)
        self.__transaction_history.append(transaction)

    def withdraw_money(self, bank_id, monetary_id, exchange_rate, amount_of_mooney):
        self.amount_of_mooney -= amount_of_mooney
        date_of_payment = datetime.date()
        if monetary == 'RUB':
            transaction = Transaction(self.__bank_id, bank_id, self.__amount_of_payment, date_of_payment)
        else:
            transaction = MonetaryTransaction(self.__bank_id, bank_id, self.__amount_of_payment, date_of_payment,
                                              monetary.Monetary[monetary], exchange_rate)
        self.__transaction_history.append(transaction)
