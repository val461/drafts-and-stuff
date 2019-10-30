#!/usr/bin/env python3


class Matrix:
    '''Implementation of square matrices.'''

    def __init__(self, rows = None):
        if rows is None:
            self._state = [Vector(self._size) for i in range(self._size)]
        else:
            self._state = rows
        self._size = len(self._state)

    #todo
    @classmethod
    def make_pointwise(cls, f):
        def pointwise_f(m, q):
            return cls(f(m_ij, q_ij))
        return pointwise_f

    #todo
    def __mul__(self, other):
        # hint: use linear_combination_of_rows
        pass


    #todo
    def linear_combination_of_rows(coefficients):
        pass


    #todo
    @Matrix.make_pointwise
    def __add__(self, other):
        return self + other


    def map(self, f):
        return [map(f, row) for row in self._state]


    def binary_map(self, other, f):
        


    def get_rows(self):
        return self._state


    def get_columns(self):
        return list(map(list, zip(*self._state))) # transpose matrix


    def get_row(self, i):
        return self.get_rows()[i]


    def get_column(self, j):
        return self.get_columns()[j]
