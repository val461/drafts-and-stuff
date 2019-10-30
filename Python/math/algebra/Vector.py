#!/usr/bin/env python3


# for len, getitem
#fixme: via metaclass?
def implement_via_state(function_name):
    def f(self, arg):
        return getattr(self._state, function_name)(arg)
    setattr(Vector, function_name, f)


def extend_binary_operation(f):
    def extended_f(v1, v2):
        assert(len(v1) == len(v2))
        return v1.binary_map(v2, f)
    return extended_f


class Vector:

    #testme
    def __init__(self, coefficients = None):
        if coefficients is None:
            # self._state = [0 for j in range(2)]
            self._state = list(range(5))
        else:
            self._state = coefficients

    implement_via_state('__len__')
    implement_via_state('__getitem__')


    # def (self):
        # return len(self._state)


    # def __getitem__(self, i):
        # return self._state[i]


    def map(self, f):
        # return Vector(map(f, self._state))
        return self.n_ary_map((), f)


    def binary_map(self, other, f):
        # return Vector([f(s, o) for s, o in zip(self._state, other._state)])
        return self.n_ary_map([other], f)


    def n_ary_map(self, others, f):
        return Vector([f(*args) for args in zip(self, *others)])


    @extend_binary_operation
    def __add__(self, other):
        return self + other


    def __eq__(self, other):
        return 


    def __repr__(self):
        return f'Vector({self._state})'


if __name__ == "__main__":
    a=Vector()
    b=a+a
