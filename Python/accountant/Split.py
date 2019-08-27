#!/usr/bin/env python3

import json

class Split:

    auto_attributes = 'account amount cleared comment'.split()

    def __init__(self, **kwargs):
        for attribute in auto_attributes:
            if attribute in kwargs:
                setattr(self, attribute, kwargs[attribute])
            else:
                setattr(self, attribute, None)


    # todo
    def check_valid(self):
        return True


    def __str__(self):
        return self.__repr__()


    # todo
    def __repr__(self):
        d = self.__dict__.copy()
        d.amount = self.amount.__repr__()
        return d.__repr__()


# if __name__ == '__main__':
