#!/usr/bin/env python3

# account
# currency
# amount

class Split:

    def __init__(self, parent, account = None, currency = None, amount = None, cleared = None):
        self.parent = parent
        self.account = account
        self.currency = currency
        self.amount = amount
        self.cleared = cleared


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
