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
            line_number = 1
            while line:
                if re.match(r'^[0-9]', line): # transaction found
                    number_of_transactions += 1
                    print(f'transaction #{number_of_transactions}')
                    # transaction header
                    matched_groups = re.match(r'^(?:([0-9]{4})/([0-9]{2})/([0-9]{2})) *([^;]*)(?:;(.*))?$', line)
                    assert matched_groups, f'header, line {line_number}'
                    date = datetime.date(*map(int, matched_groups.group(1, 2, 3)))
                    matched = dict(zip(['description', 'tags'], matched_groups.group(4, 5)))
                    tags = dict(tag.split(': ') for tag in matched['tags'].strip().split(','))
                    if 'seller' in tags:
                        sellers = [tags['seller']]
                        del tags['seller']
                    else:
                        sellers = None
                    transaction = Transaction(comment = matched['description'], date = date, other_parties = sellers, tags = tags, cleared = None)
                    line = ledger_file.readline()
                    line_number += 1
                    # splits
                    while len(line) > 1:   # line bigger than just '\n'
                        matched_groups = re.match(r'^ *([^ ]+) *([-+]? *[0-9.]+) *([^ ;]+)(?:;(.*))?$', line)
                        assert matched_groups, f'split, line {line_number}'
                        matched = dict(zip(['account', 'amount', 'currency', 'comment'], matched_groups.group(*range(1, 5))))
                        transaction.new_split(**matched)
                        line = ledger_file.readline()
                        line_number += 1
                    # check there is at least one split
                    assert transaction.splits, f'no splits, line {line_number}'

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
