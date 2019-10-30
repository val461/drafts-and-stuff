#!/usr/bin/env python3

import random


def number_of_duplicates(l):
    return len(l) - len(set(l))


def has_duplicates(l):
    return number_of_duplicates(l) > 0


def random_pop(l):
    '''Pops a random item from a list.'''
    return l.pop(random.randrange(len(l)))


class Grid:

    none = 'N'

    def __init__(self, size = 2):
        self._size = size
        self._total_size = self._size ** 2
        self._state = [[Grid.none for j in range(self._size)] for i in range(self._size)]
        self._acceptable_values = set(range(1, self._size + 1))
        self._all_cell_indices = [(i, j) for i in range(self._size) for j in range(self._size)]


    def play(self):
        self.erase()
        self.show()

        print('Now filling unfilled cells validly.')
        self.steps(self.fill_unfilled_cells, validly = True, n_per_step = None)
        if(len(self.get_indices_of_unfilled_cells()) < 1):
            print('Done.')
            return

        print('Now filling unfilled cells invalidly.')
        self.steps(self.fill_unfilled_cells, validly = False)
        print('No more unfilled cells.')

        while True:
            print('Now rectifying filled cells.')
            self.steps(self.fill_invalid_cells, validly = True)
            l = len(self.get_indices_of_invalid_cells())
            if(l < 1):
                print('Done.')
                return
            print(f'{l} invalid cells remain.')
            print('Now transforming an invalid cell.')
            self.steps(self.fill_invalid_cells, validly = False, max_steps = 1)


    def steps(self, f, validly, n_per_step = 1, max_steps = None):
        i = 0
        while f(n_max = n_per_step, validly = validly) > 0:
            self.show()
            i += 1
            input('next [enter]')
            if max_steps and i >= max_steps:
                return


    def erase(self):
        for i in range(self._size):
            for j in range(self._size):
                self.set_cell(i, j, Grid.none)


    def fill_unfilled_cells(self, n_max = None, validly = True):
        '''Returns the number of modifications.'''
        return self.fill_cells(self.get_indices_of_unfilled_cells(), n_max, validly)


    def fill_invalid_cells(self, n_max = None, validly = True):
        '''Returns the number of modifications.'''
        return self.fill_cells(self.get_indices_of_invalid_cells(), n_max, validly)


    def fill_cells(self, cells = [], n_max = None, validly = True):
        '''Returns the number of modifications.

        (Modifies 'cells' in place.)
        (Cells are filled in a random order.)'''

        if n_max is None:
            n_max = len(cells)

        if validly:
            fill = self.fill_cell_validly
        else:
            fill = self.fill_cell_randomly

        n_filled = 0
        while n_filled < n_max and len(cells) >= 1:
            if fill(*random_pop(cells)):
                n_filled += 1

        return n_filled


    def fill_cell_randomly(self, i, j):
        self.set_cell(i, j, random.randint(1, self._size))
        return True


    def fill_cell_validly(self, i, j):
        '''Returns True if a modification was performed.'''
        acceptable_values = self.acceptable_values_for_cell(i, j)
        if len(acceptable_values) < 1:
            return False
        self.set_cell(i, j, random.choice(list(acceptable_values)))
        return True


    def is_cell_unfilled(self, i,j):
        return self.get_cell(i, j) == Grid.none


    def is_cell_filled(self, i,j):
        return not self.is_cell_unfilled(i, j)


    def is_cell_invalid(self, i,j):
        value = self.get_cell(i, j)
        return self.is_cell_filled(i, j) and (self.get_row(i).count(value) >= 2 or self.get_column(j).count(value) >= 2)


    def get_indices_of_invalid_cells(self):
        return self.filter_cell_indices(self.is_cell_invalid)


    def get_indices_of_unfilled_cells(self):
        return self.filter_cell_indices(self.is_cell_unfilled)


    def filter_cell_indices(self, indice_filter):
        return list(filter(lambda x : indice_filter(x[0], x[1]), self._all_cell_indices))


    # def get_indices_of_invalid_sections_in_list(self, list_of_sections):
        # return [i for (i, s) in enumerate(list_of_sections) if has_duplicates(s)]


    # def get_indices_of_invalid_sections(self):
        # return dict(zip(['rows', 'columns'], map(get_indices_of_invalid_sections_in_list, [self.get_rows(), self.get_columns()])))


    def acceptable_values_for_cell(self, i, j):
        return self._acceptable_values - self.get_values_in_row(i) - self.get_values_in_column(j)


    def set_cell(self, i, j, v):
        self._state[i][j] = v


    def get_cell(self, i, j):
        return self._state[i][j]


    def get_rows(self):
        return self._state


    def get_columns(self):
        return list(map(list, zip(*self._state))) # transpose matrix


    def get_row(self, i):
        return self.get_rows()[i]


    def get_column(self, j):
        return self.get_columns()[j]


    def get_values_in_row(self, i):
        return set(self.get_row(i)) - {Grid.none}


    def get_values_in_column(self, j):
        return set(self.get_column(j)) - {Grid.none}


    def get_sections_as_flat_lists(self):
        return self.get_rows() + self.get_columns()


    def get_entropy(self):
        return sum(map(number_of_duplicates, self.get_sections_as_flat_lists()))


    # def is_valid(self):
        # return all(map(no_duplicates, self.get_rows() + self.get_columns()))
        # # return all(map(no_duplicates, self.get_rows() + self.get_columns() + self.get_regions_flattened()))


    def __str__(self):
        return '\n' + '\n'.join([' '.join(map(str, l)) for l in self._state]) + '\n'


    def show(self):
        print(self)


if __name__ == '__main__':
    g = Grid(4)
    g.play()
