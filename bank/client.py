from account import BankAccount


class Client:
    def __init__(self, client_id, client_name):
        self.__client_id = client_id
        self.__client_name = client_name
        self.__accounts = {}

    def get_client_name(self):
        return self.__client_name

    def open_account(self, account_id, bank_id, amount_of_mooney=0):
        account = BankAccount(account_id, bank_id, self.__client_id, amount_of_mooney)
        self.__accounts[account_id] = account
        return account

    def close_account(self, account_id):
        del self.__accounts[account_id]

    def get_accounts(self):
        return self.__accounts

    def get_total_amount_of_mooney(self):
        return sum(i.get_amount_of_mooney() for i in self.__accounts.values())

    def occur_bank_ransfer(self, sending_account_id, sending_bank_id, receiving_account_id, receiving_bank_id,
                           amount_of_mooney, monetary='RUB', exchange_rate=''):
        self.__accounts[sending_account_id].withdraw_money(receiving_bank_id, amount_of_mooney, monetary,
                                                           exchange_rate)
        self.__accounts[receiving_account_id].deposit_mooney(sending_bank_id, amount_of_mooney, monetary,
                                                             exchange_rate)
