#!/usr/bin/env python3

def _remove_whitespace(string):
    return ''.join(string.split())


#todo
# implement operations via matrix and vector operations

class Complex:
    '''Was meant to become an implementation of complex numbers. Allows real and imaginary parts to be Python integers, or another Python numeric type.'''

    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag


    #testme
    @classmethod
    def from_string(cls, string, number_interpreter = int)
        string_parts = _remove_whitespace(string).split('+')
        if len(string_parts) == 2:
            real = number_interpreter(string_parts[0])
            assert(string_parts[1][-1] == 'i')
            imag = number_interpreter(string_parts[1][:-1])
        else:
            assert(len(string_parts) == 1)
            if string_parts[0][-1] == 'i':
                real = 0
                imag = number_interpreter(string_parts[0][:-1])
            else:
                real = 0
                imag = number_interpreter(string_parts[0])
        return cls(real, imag)


    def __repr__(self):
        return f'Complex({self.real}, {self.imag})'


    def __str__(self):
        if self.imag == 0:
            return f'{self.real}'
        elif self.real == 0:
            return f'{self.imag}i'
        else:
            return f'{self.real}+{self.imag}i'


    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)


    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)


    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)


