#!/usr/bin/env python3

# todo:
    # transaction
        # splits
            # offer the possibility to set default split amounts as fractions of previous split amounts of this transaction
        # date
        # comment
        # tags
            # imply rules
        # other_parties
            # store or person or N/A
        # to be refunded
            # amount
                # percentage
            # debtor

import Split

class Transaction:

    def __init__(self, comment = None, default_currency = None, date = None, cleared = False, other_parties = None, tags = None):
        self.comment = comment
        self.default_currency = default_currency
        self.date = date
        self.cleared = cleared
        self.other_parties = other_parties
        self.tags = tags
        self.splits = []

        # DELETE ME ONCE IMPORTATION IS OVER
        self.product_details = {'name': None, 'amount': None, 'unit': None}


    # todo
    def add_split(self, **args):
        self.splits.append(Split(self, **args))

    # todo
    def seems_valid(self):
        # check that parameters are set with correct types
        return True


    # todo
    def __str__(self):
        return ''


    # todo
    def __repr__(self):
        # (fixme: ambiguous output)
        return self.__str__()
    

# if __name__ == '__main__':
