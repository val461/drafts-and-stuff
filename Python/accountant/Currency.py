#!/usr/bin/env python3

# symbol
# precision
    # number of digits after period
        # int >= 0 or 'unlimited'

class Currency:

    defaults = {precision: 2, side: 'right'}

    def __init__(self, symbol = None, precision = None, side = None):

        if precision is None:
            precision = defaults.precision
        if side is None:
            side = defaults.side

        self.symbol = symbol
        self.precision = precision
        self.side = side


    # fixme
    def truncate_amount(self, amount):
        if precision == 'unlimited':
            result = amount
        else:
            result = round amount to `precision` digits
        return result


    # todo
    def format_amount(self, amount, side = None):
        # if side == 'right':
        return f'{truncate_amount(amount)} {self.symbol}'
        # elif side == 'left':


    # todo
    def __str__(self):
        return ''


    # todo
    def __repr__(self):
        # (fixme: ambiguous output)
        return self.__str__()
    

# if __name__ == '__main__':
