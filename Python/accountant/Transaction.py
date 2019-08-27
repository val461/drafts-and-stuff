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

    def __init__(self, comment = None, date = None, cleared = None, other_parties = None, tags = None, product_name = None, product_amount = None, product_unit = None):
        self.comment = comment
        self.date = date
        self.cleared = cleared
        self.other_parties = other_parties
        self.tags = tags
        self.splits = []

        # DELETE THESE 3 ARGS ONCE IMPORTATION IS OVER
        self.product_name = product_name
        self.product_amount = product_amount
        self.product_unit = product_unit


    def new_split(self, **kwargs):
        self.splits.append(Split(**kwargs))

    # todo
    def check_valid(self):
        # check that parameters are set with correct types
        return True


    # check me
    def to_dictionary(self):
        result = self.__dict__.copy()
        result['splits'] = [split.__repr__() for split in self.splits]
        return result


    # todo
    def __str__(self):
        return ''


    # todo
    def __repr__(self):
        # (fixme: ambiguous output)
        return self.__str__()
    

# if __name__ == '__main__':
