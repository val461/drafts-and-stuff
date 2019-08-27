#!/usr/bin/env python3

# symbol
# precision
    # number of digits after period
        # int >= 0 or 'unlimited'

# todo
    # decimal separator
    # generalize auto_attributes to use it with the other modules
        # mix-in? class decorator?

class Amount:

    constant_defaults = dict(symbol = '€', precision = 2, symbol_side = 'right')
    dynamic_defaults = dict(l = lambda : [])    # useless here, shown only for showcasing purposes
    auto_attributes = 'value symbol precision symbol_side'.split()

    def __init__(self, **kwargs):
        for attribute in auto_attributes:
            if attribute in kwargs:
                setattr(self, attribute, kwargs[attribute])
            elif attribute in Amount.constant_defaults:
                setattr(self, attribute, Amount.constant_defaults[attribute])
            elif attribute in Amount.dynamic_defaults:
                setattr(self, attribute, Amount.dynamic_defaults[attribute]())
            else:
                setattr(self, attribute, None)

    # fixme
    def truncate_value(self, precision = None):
        if precision == 'unlimited':
            result = self.value
        else:
            result = round self.value to `precision` digits
        return result


    # todo
    def __str__(self, precision = None, side = None):
        # if side == 'right':
        return f'{truncate_amount(amount)} {self.symbol}'
        # elif side == 'left':


    # todo
    def __repr__(self):
        # (goal: unambiguous output)
        return self.__str__()
    

# if __name__ == '__main__':
