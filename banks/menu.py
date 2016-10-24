from banks.bank import Bank
import sys, uuid


def main():
    bank = Bank()

    while (1):
        print("Bank:\n")
        print('List of accounts - la')
        print('List of clients - lc')
        print('Total amount of money - mb')
        print('Add client - c <client_name>')
        print('Open account - a <client_id> <amount_of_mooney> (default - 0)')
        print("Clients:\n")
        print('Get total amount of money - t')
        print(
            'Occur bank transfer - o <sending_account_id> <receiving_account_id> <amount_of_money> <monetary> (default - "RUB") <exchange_rate>')
        print('Get amount of money - mc <account_id>')
        print('Get transaction history - h <account_id>')
        print('Exit - e')

        input = sys.stdin.readline().strip()
        if input == 'la':
            accounts = bank.get_accounts()
            if accounts:
                print('Accounts:')
                for account in accounts:
                    print(account)
            else:
                print('There are not accounts.')
                continue

        elif input == 'lc':
            clients = bank.get_clients()
            if clients:
                print('Clients:')
                for client in clients:
                    print(client)
            else:
                print('There are not clients.')
                continue

        elif input == 'mb':
            print(bank.get_total_amount_of_mooney())

        elif input.startswith('a'):
            try:
                inputs = input.split()
                client_id = uuid.UUID(inputs[1])
                try:
                    amount_of_mooney = inputs[2]
                    if amount_of_mooney < 0:
                        print('Amount of money must be more than zero! Try again.')
                        continue
                except:
                    amount_of_mooney = 0
                try:
                    account_id = bank.open_account(client_id, amount_of_mooney)
                    print('Account %s added.' % (account_id))
                except:
                    print('There is not such client id. Try again.')
            except:
                print('Empty client id. Try again.')
                continue

        elif input.startswith('c'):
            try:
                client_name = input.split()[1]
                bank.add_client(client_name)
                print('Client %s added.' % (client_name))
            except:
                print('Empty client name. Try again.')
                continue

        elif input == 't':
            try:
                print('Total amount of money:', bank.get_amount_of_mooney_by_client_id(client_id))
            except:
                print('There is not such client id. Try again.')

        elif input.startswith('mc'):
            account_id = uuid.UUID(input.split()[1])
            try:
                print('Amount of money:', accounts[account_id].get_amount_of_mooney())
            except:
                print('There is not such account id. Try again.')

        elif input.startswith('h'):
            account_id = uuid.UUID(input.split()[1])
            transactions = bank.get_transaction_history_by_account_id(account_id)
            if transactions:
                print('Transaction history:')
                for transaction in transactions:
                    print(transaction)

        elif input.startswith('o'):
            inputs = input.split()
            sending_account_id = uuid.UUID(inputs[1])
            receiving_account_id = uuid.UUID(inputs[2])
            amount_of_money = inputs[3]
            try:
                monetary = input.split()[4]
                exchange_rate = input.split()[5]
            except:
                monetary = 'RUB'
                exchange_rate = ''
            bank.occur_bank_ransfer(sending_account_id,
                                    receiving_account_id,
                                    amount_of_money,
                                    monetary=monetary,
                                    exchange_rate=exchange_rate)
