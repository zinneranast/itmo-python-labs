from banks.bank import Bank
import sys, uuid


def main():
    bank = Bank()
    print("Bank:")
    print('List of accounts - la')
    print('List of clients - lc')
    print('Total amount of money - mb')
    print('Add client - c <client_name>')
    print('Open account - a <client_id> <amount_of_mooney> (default - 0)')
    print('Set decision - d <transaction_id> <decision> (true or false)')
    print("\nClients:")
    print('Get total amount of money - t <client_id>')
    print(
        'Occur bank transfer - o <sending_account_id> <receiving_account_id> <amount_of_money> <monetary> (default - "RUB") <exchange_rate>')
    print('Get amount of money - mc <account_id>')
    print('Get transaction history - h <account_id>')
    print('Exit - e')

    while (1):
        input = sys.stdin.readline().strip()
        if input == 'la':
            accounts = bank.get_accounts()
            if accounts:
                print('Accounts:')
                for account in accounts:
                    print(account.get_account_id(), ": client",
                          bank.get_client(account.get_client_id()).get_client_name(),
                          ": amount of money", account.get_amount_of_mooney())
            else:
                print('There are not accounts.')
                continue

        elif input == 'lc':
            clients = bank.get_clients()
            if clients:
                print('Clients:')
                for client in clients:
                    print(client.get_client_id(), client.get_client_name())
            else:
                print('There are not clients.')
                continue

        elif input == 'mb':
            print(bank.get_total_amount_of_mooney())
            continue

        elif input.startswith('a'):
            try:
                inputs = input.split()
                client_id = uuid.UUID(inputs[1])
                try:
                    amount_of_mooney = float(inputs[2])
                    if amount_of_mooney < 0:
                        print('Amount of money must be more than zero! Try again.')
                        continue
                except:
                    amount_of_mooney = 0
                try:
                    account_id = bank.open_account(client_id, amount_of_mooney=amount_of_mooney)
                    print('Account %s added.' % (account_id))
                    continue
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
                continue
            except:
                print('Empty client name. Try again.')
                continue

        elif input.startswith('t'):
            try:
                client_id = uuid.UUID(input.split()[1])
                print('Total amount of money:', bank.get_amount_of_mooney_by_client_id(client_id))
                continue
            except:
                print('There is not such client id. Try again.')

        elif input.startswith('mc'):
            try:
                account_id = uuid.UUID(input.split()[1])
                print('Amount of money:', bank.get_amount_of_mooney_by_account_id(account_id))
                continue
            except:
                print('There is not such account id. Try again.')

        elif input.startswith('h'):
            account_id = uuid.UUID(input.split()[1])
            transactions = bank.get_transaction_history_by_account_id(account_id)
            if transactions:
                print('Transaction history:')
                for transaction in transactions:
                    print(transaction.get_transaction_id(), ": from ", transaction.get_sending_account_id(),
                          ": to ", transaction.get_receiving_account_id(), ": amount of payment ",
                          transaction.get_amount_of_payment(), ": date ", transaction.get_date_of_payment())
            else:
                print('Transaction history is empty.')
            continue

        elif input.startswith('o'):
            inputs = input.split()
            sending_account_id = uuid.UUID(inputs[1])
            receiving_account_id = uuid.UUID(inputs[2])
            amount_of_money = float(inputs[3])
            try:
                monetary = input.split()[4]
                exchange_rate = float(input.split()[5])
                print('Bank transfer is requested.')
            except:
                monetary = 'RUB'
                exchange_rate = ''
                print('Bank transfer is occured.')
            bank.occur_bank_ransfer(sending_account_id,
                                    receiving_account_id,
                                    amount_of_money,
                                    monetary=monetary,
                                    exchange_rate=exchange_rate)
            continue

        elif input.startswith('d'):
            try:
                inputs = input.split()
                transaction_id = uuid.UUID(inputs[1])
                decision = inputs[2]
                if decision == 'true':
                    print('Bank transfer is occured.')
                    bank.bank_decision(transaction_id, True)
                elif decision == 'false':
                    print('Bank transfer is declined.')
                    bank.bank_decision(transaction_id, False)
                else:
                    print('Try again.')
                continue
            except:
                print('There is not such transaction id. Try again.')

        elif input == 'e':
            exit()


main()
