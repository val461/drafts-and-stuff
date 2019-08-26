#!/usr/bin/env python3

# ? delete me once importation is over
import datetime, re
import Transaction

class Ledger:

    def __init__(self):
        self.accounts = []
        self.currencies = []
        self.default_currency = Currency(symbol = '€', precision = 2, side = 'right')
        self.currencies.append(self.default_currency)
        self.transactions = []


    def save(self, filename = 'ledger.txt'):
        with open(filename, 'w') as ledger_file:
            ledger_file.write(self.__repr__())


    # todo
    @staticmethod
    def new_from_file(filename = 'ledger.txt'):
        pass


    # delete me once importation is over
    # todo
    @staticmethod
    def import_from_hledger(filename = '/home/val/Documents/Vie pratique/finances/Comptabilité/hledger/1.journal'):
        ledger = Ledger()
        number_of_transactions = 0

        with open(filename, 'r') as ledger_file:
            line = ledger_file.readline()
            while line:
                if re.match(r'^[0-9]', line):
                    number_of_transactions += 1
                    print(f'transactions #{number_of_transactions}')
                    matched_groups = re.match(r'^(?:([0-9]{4})/([0-9]{2})/([0-9]{2})) *([^;]*)(?:;(.*))?$', line)
                    assert(matched_groups)
                    date = datetime.date(*map(int, matched_groups.group(1, 2, 3)))
                    matched = dict(zip(['description', 'tags'], matched_groups.group(4, 5)))
                    tags = dict(tag.split(': ') for tag in matched['tags'].strip().split(','))
                    if 'seller' in tags:
                        sellers = [tags['seller']]
                    else:
                        sellers = None
                    transaction = Transaction(comment = matched['description'], default_currency = self.default_currency, date = date, cleared = False, other_parties = sellers, tags = tags)
                    line = ledger_file.readline()
                    if re.match(r'^ *([a-zA-Z0-9:]+) *([-+]? *[0-9]+) *([^.]+)()', line):# todo: float or int, semicolon or not, comment or not

                line = ledger_file.readline()

        print(f'number_of_transactions: {number_of_transactions}')
        return ledger


    # todo
    def __str__(self):
        return ''


    # todo
    def __repr__(self):
        # (fixme: ambiguous output)
        return self.__str__()


    # todo
    def new_transaction(self):
        pass


# if __name__ == "__main__":
    # pass
