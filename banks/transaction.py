class Transaction:
    def __init__(self, transaction_id, sending_account_id, receiving_account_id, amount_of_payment, date_of_payment):
        self.__transaction_id = transaction_id
        self.__sending_account_id = sending_account_id
        self.__receiving_account_id = receiving_account_id
        self.__amount_of_payment = float(amount_of_payment)
        self.__date_of_payment = date_of_payment

    def get_transaction_id(self):
        return self.__transaction_id

    def get_sending_account_id(self):
        return self.__sending_account_id

    def get_receiving_account_id(self):
        return self.__receiving_account_id

    def get_amount_of_payment(self):
        return self.__amount_of_payment

    def get_date_of_payment(self):
        return self.__date_of_payment


class MonetaryTransaction(Transaction):
    def __init__(self, transaction_id, sending_account_id, receiving_account_id, amount_of_payment, date_of_payment, monetary_id, exchange_rate):
        super().__init__(transaction_id, sending_account_id, receiving_account_id, amount_of_payment, date_of_payment)
        self.__monetary_id = monetary_id
        self.__exchange_rate = float(exchange_rate)

    def get_monetary_id(self):
        return self.__monetary_id

    def get_exchange_rate(self):
        return self.__exchange_rate

    def get_amount_of_payment_in_rubles(self):
        return float(self.get_amount_of_payment()) * float(self.__exchange_rate)
