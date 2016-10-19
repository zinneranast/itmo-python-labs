class Transaction:
    def __init__(self, sending_bank, receiving_bank, amount_of_payment, date_of_payment):
        self.__sending_bank = sending_bank
        self.__receiving_bank = receiving_bank
        self.__amount_of_payment = amount_of_payment
        self.__date_of_payment = date_of_payment

    def get_sending_bank(self):
        return self.__sending_bank

    def get_receiving_bank(self):
        return self.__receiving_bank

    def get_amount_of_payment(self):
        return self.__amount_of_payment

    def get_date_of_payment(self):
        return self.__date_of_payment


class MonetaryTransaction(Transaction):
    def __init__(self, sending_bank, receiving_bank, amount_of_payment, date_of_payment, monetary_id, exchange_rate):
        super().__init__(self, sending_bank, receiving_bank, amount_of_payment, date_of_payment)
        self.__monetary_id = monetary_id
        self.__exchange_rate = exchange_rate

    def get_monetary_id(self):
        return self.__monetary_id

    def get_exchange_rate(self):
        return self.__exchange_rate

    def get_amount_of_payment_in_rubles(self):
        return self.__amount_of_payment * self.__exchange_rate
