#!/usr/bin/env python3

class GroupElement:
#todo
#   invert

    def __init__(self, group_table, name):
        self._group_table = group_table
        self._name = name


    #todo
    def __mul__(self, other):
        pass


    #todo
    def __pow__(self, integer):
        pass


class GroupTableCreator:
#todo
    # neutral element
    # commutative
    # inverses
    # implementation of operation
    pass


class GroupTable:

    def __init__(self, size = None, element_strings = None, operation_string = ''):

        if size is None:
            assert(element_strings)
            self._size = len(element_strings)
        else:
            self._size = size

        if element_strings is None:
            assert(self._size)
            self._element_strings = map(str, range(self._size))
        else:
            self._element_strings = element_strings


    #testme
    def print_subgroups_and_normality(self):
        for subgroup in self.get_subgroups()
            print(subgroup, self.is_subgroup_normal(subgroup))


    #todo
    def get_subgroups(self):
        pass


    #todo
    def is_subgroup_normal(self, subgroup):
        pass


    #todo
    def is_abelian(self):
        pass


    #todo
    def get_center(self):
        pass


    #todo
    def do_they_commute(self, a, b):
        pass


    #todo
    def set_sort_order(self, new_element_strings):
        pass


    #todo
    def __str__(self):
        pass
        # return '\n' + '\n'.join([' '.join(map(str, l)) for l in self._state]) + '\n'


    def show(self):
        print(self)


# if __name__ == '__main__':
