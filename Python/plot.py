#!/usr/bin/env python3

'''Freely adapted from
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
https://www.geeksforgeeks.org/graph-plotting-python-set-2/
consulted on 2022-12-10.
'''

import matplotlib.pyplot as pyplot
import random

def load_iso88591(filename):
    my_file = open(filename, 'r', encoding='iso-8859-1')
    content = my_file.read()
    my_file.close()
    return content

def parse_grade(grade):
    if not grade or grade == 'ABI' or grade == 'ABJ':
        return 0
    else:
        return float(grade)

# parse csv file from Thor
raw_data = [line.split(';') for line in load_iso88591('plot_data/MA0101_notes_bilan_S1A4.csv').splitlines()]
names = [row[1] for row in raw_data]
first_column = 4
last_column = 6
evaluation_labels = raw_data[0][first_column : last_column + 1]
raw_grades = [row[first_column : last_column + 1] for row in raw_data[1:]]
all_grades = [list(map(parse_grade, row)) for row in raw_grades]

# plotting

fig = pyplot.figure()

for k in range(0, len(all_grades[0])):
    # 1 histogram plot per evaluation
    grades = [row[k] for row in all_grades]
    plot = fig.add_subplot(2, 3, k+1)
    plot.hist(x = grades, bins = 8, range = (0, 20), histtype = 'bar')

# 1 bar chart for all evaluations, with names

# adjusting space between subplots
# fig.subplots_adjust(hspace=.5,wspace=0.5)

pyplot.show()


'''
data = [random.randint(0,19)+random.random() for k in range(26)]

# plotting a histogram
# optional args: color = 'green', rwidth = 0.8
pyplot.hist(x = data, bins = 10, range = (0, 20), histtype = 'bar')

pyplot.xlabel('notes')
pyplot.ylabel('effectifs')
# pyplot.title('My histogram')

pyplot.show()
'''
