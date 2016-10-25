class BankAccount:
    def __init__(self, account_id, client, amount_of_mooney):
        self.__account_id = account_id
        self.__client = client
        self.__amount_of_mooney = float(amount_of_mooney)

    def get_account_id(self):
        return self.__account_id

    def get_client_id(self):
        return self.__client.get_client_id()

    def get_amount_of_mooney(self):
        return self.__amount_of_mooney

    def deposit_mooney(self, amount_of_mooney):
        self.__amount_of_mooney += float(amount_of_mooney)

    def withdraw_money(self, amount_of_mooney):
        self.__amount_of_mooney -= float(amount_of_mooney)
