#!/usr/bin/env python3

# The Lost Symbol, Dan Brown, page 273
# What if Robert read the message in the wrong orientation?
# This is the point of the present script.

import copy
import numpy as np
from string import ascii_lowercase as alphabet


def main():

    message = 'S00J12A11S01 A00S10S01J11 A02S00A00S00 S11S01J11J00'
    tables = makeTables(message)
    print(decrypt(tables))
    for i in range(3):
        tables = rotate_tables_90_CW(tables)
        print('\n'+decrypt(tables))


def makeTables(message):

    return {
        'A': string_to_table(alphabet[0:9]),
        'J': string_to_table(alphabet[9:18]),
        'S': string_to_table('sutv'),
        'W': string_to_table('wyxz'),
        'message': message_to_table(message)
    }


def decrypt(tables):

    return '\n'.join([
        ''.join([
            tables[key][int(row)][int(col)]
            for i in range(len(line))
            for key, row, col in [line[i]]
        ])
        for line in tables['message']
    ])


def rotate_tables_90_CW(tables):

    return {table_name: rotate_table_90_CW(table) for table_name, table in tables.items()}


def rotate_table_90_CW(table):

    coords = np.array([[i,j] for i in range(len(table)) for j in range(len(table[i]))])
    center=centroid(coords)

    new_coords =  center + np.apply_along_axis(rotate_point_90_CW, 1, coords - center)

    new_table = copy.deepcopy(table)
    for k in range(len(new_coords)):
        x, y = map(int, coords[k])
        x_new, y_new = map(int, new_coords[k])
        new_table[x_new][y_new] = table[x][y]

    return new_table


def rotate_point_90_CW(point):
    return np.array([point[1],-point[0]])


def centroid(points):

    return np.sum(points,0) / np.size(points,0)


def string_to_table(string):

    return unflatten(list(string), int(np.sqrt(len(string))))


def message_to_table(message):

    return [unflatten(line, 3) for line in message.split()]


def unflatten(l, sublist_size):
    '''Convert 1D list into 2D list.

    'sublist_size' (positive integer) should be a divisor of len(l).
    '''
    return [l[i:i+sublist_size] for i in range(0, len(l) - sublist_size + 1, sublist_size)]


if __name__ == '__main__':
    main()
