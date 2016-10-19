from banks.bank import Bank
import sys, uuid


def main():
    banks = {}
    clients = {}
    while (1):
        print("Banks - b\nClients - c\nExit - e")
        input = sys.stdin.readline().strip()
        if input == 'b':
            print('List of banks - l')
            print('Get more information about bank - i <bank_id>')
            print('Add bank - a <bank_name>')
            print('Remove bank - r <bank_id>')
            print('Exit - e')
            input = sys.stdin.readline().strip()
            if input == 'l':
                if banks:
                    for bank_id, bank in banks.items():
                        print(bank_id, bank.get_name())
                else:
                    print('There are not banks.')
                    continue
            elif input.startswith('i'):
                try:
                    bank_id = uuid.UUID(input.split()[1])
                except:
                    print('Empty bank id. Try again.')
                    continue
                print('List of accounts - la')
                print('List of clients - lc')
                print('Total amount of money - m')
                print('Add account - a <client_id> <amount_of_mooney> (default - 0)')
                print('Add client - c <client_name>')
                print('Exit - e')
                input = sys.stdin.readline().strip()
                if input == 'la':
                    if bank_id in banks:
                        accounts = banks[bank_id].get_list_of_accounts()
                        if accounts:
                            print('Accounts:')
                            for account_id, account in accounts:
                                print(account_id, account)
                        else:
                            print('There are not accounts.')
                            continue
                    else:
                        print('This bank does not exist. Try again.')
                        continue
                elif input == 'lc':
                    if bank_id in banks:
                        clients = banks[bank_id].get_list_of_clients()
                        if clients:
                            print('Clients:')
                            for client_id, client in clients:
                                print(client_id, client)
                        else:
                            print('There are not clients.')
                            continue
                    else:
                        print('This bank does not exist. Try again.')
                        continue
                elif input == 'm':
                    if bank_id in banks:
                        print(banks[bank_id].get_total_amount_of_mooney())
                    else:
                        print('This bank does not exist. Try again.')
                        continue
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
                        if banks[bank_id].get_client(client_id):
                            banks[bank_id].add_account(client_id, amount_of_mooney)
                            print('Account added.')
                        else:
                            print('There is not such client id. Try again.')
                    except:
                        print('Empty client id. Try again.')
                        continue
                elif input.startswith('c'):
                    try:
                        client_name = input.split()[1]
                        banks[bank_id].add_client(client_name)
                        print('Client %s added.' % (client_name))
                    except:
                        print('Empty client name. Try again.')
                        continue
                elif input == 'e':
                    exit()
                else:
                    continue
            elif input.startswith('a'):
                bank_id = uuid.uuid4()
                try:
                    bank_name = input.split()[1]
                    bank = Bank(bank_id, bank_name)
                    banks[bank_id] = bank
                    print('Bank %s added.' % (bank.get_name()))
                except:
                    print('Empty bank name. Try again.')
                    continue
            elif input.startswith('r'):
                try:
                    bank_id = uuid.UUID(input.split()[1])
                    del banks[bank_id]
                    print('Bank %s removed.' % (bank.get_name()))
                except:
                    print('Empty bank id. Try again.')
                    continue
            elif input == 'e':
                exit()
            else:
                continue
        elif input == 'c':
            print('List of clients - l <bank_id>')
            print('Add client - a <bank_id> <client_name>')
            print('Remove client - r <bank_id> <client_id>')
            print('Get info about client - i <bank_id> <client_id>')
            print('Exit - e')
            input = sys.stdin.readline().strip()
            if input.startswith('l'):
                bank_id = uuid.UUID(input.split()[1])
                clients = banks[bank_id].get_list_of_clients()
                if clients:
                    print('Clients:')
                    for client in clients:
                        print(client)
            elif input.startswith('a'):
                inputs = input.split()
                bank_id = uuid.UUID(inputs[1])
                client_name = inputs[2]
                banks[bank_id].add_client(client_name)
            elif input.startswith('r'):
                inputs = input.split()
                bank_id = uuid.UUID(inputs[1])
                client_id = uuid.UUID(inputs[2])
                banks[bank_id].remove_client(client_id)
            elif input.startswith('i'):
                bank_id = uuid.UUID(input.split()[1])
                client_id = uuid.UUID(input.split()[2])
                accounts = banks[bank_id].get_client_accounts()
                for account_id, account in accounts.items():
                    print(account_id, account)
                print('Get total amount of money - t')
                print(
                    'Occur bank transfer - o <sending_account_id> <sending_bank_id> <receiving_account_id> <receiving_bank_id> <amount_of_money> <monetary> <exchange_rate>')
                print('Get amount of money - m <account_id>')
                print('Get transaction history - h <account_id>')
                print('Exit - e')
                input = sys.stdin.readline().strip()
                if input == 't':
                    print('Total amount of money:', banks[bank_id].get_client_total_amount_of_money(client_id))
                elif input.startswith('o'):
                    inputs = input.split()
                    sending_account_id = uuid.UUID(inputs[1])
                    sending_bank_id = uuid.UUID(inputs[2])
                    receiving_account_id = uuid.UUID(inputs[3])
                    receiving_bank_id = uuid.UUID(inputs[4])
                    amount_of_money = inputs[5]
                    try:
                        monetary = input.split()[6]
                        exchange_rate = input.split()[7]
                    except:
                        monetary = 'RUB'
                        exchange_rate = ''
                    banks[sending_bank_id].occur_bank_ransfer(sending_account_id, receiving_account_id,
                                                              amount_of_money, receiving_bank_id=receiving_bank_id,
                                                              monetary=monetary,
                                                              exchange_rate=exchange_rate)
                    banks[receiving_bank_id].occur_bank_ransfer(sending_account_id, receiving_account_id,
                                                                amount_of_money, sending_bank_id=sending_bank_id,
                                                                monetary=monetary,
                                                                exchange_rate=exchange_rate)
                elif input.startswith('m'):
                    account_id = uuid.UUID(input.split()[1])
                    print('Amount of money:', accounts[account_id].get_amount_of_mooney())
                elif input.startswith('h'):
                    account_id = uuid.UUID(input.split()[1])
                    transactions = accounts[account_id].get_transaction_history()
                    if transactions:
                        print('Transaction history:')
                        for transaction in transactions:
                            print(transaction)
                elif input == 'e':
                    exit()
                else:
                    continue
            elif input == 'e':
                exit()
            else:
                continue
        elif input == 'e':
            exit()
        else:
            continue


main()
