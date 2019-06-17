#!/usr/bin/env python3

import random


def number_of_duplicates(l):
    return len(l) - len(set(l))


def has_duplicates(l):
    return number_of_duplicates(l) > 0


class Cell:

    def __init__(self, i=0, j=0, v = None, solid = False):
        # self._i = i
        # self._j = j
        if not v:
            v = Grid.none
        self._v = v
        self._solid = solid


    def get_value(self):
        return self._v


    def set_value(self, v):
        assert(self.is_soft() or self.is_unfilled())
        self._v = v


    # def get_position(self):
        # return self._i, self._j


    # def get_row_indice(self):
        # return self._i


    # def get_column_indice(self):
        # return self._j


    def is_solid(self):
        return self._solid


    def is_soft(self):
        return not self.is_solid()


    def is_filled(self):
        return self.get_value() != Grid.none


    def is_unfilled(self):
        return not self.is_filled()


class Grid:

    none = 'N'

    def __init__(self, size = 2):
        self._size = size
        self._state = [[Cell(i, j) for j in range(self._size)] for i in range(self._size)]
        self._acceptable_values = set(range(1, self._size + 1))


    def pick_and_fill_solid_cells(self, n_max = 1):
        return self.fill_cells(self.get_indices_of_unfilled_cells(), n_max)


