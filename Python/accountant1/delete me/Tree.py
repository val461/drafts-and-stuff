#!/usr/bin/env python3

class Tree:
    tab = 4 * " "

    def __init__(self, description="", children=[]):
        self.description = description
        self.children = children

    def to_string(self, min_indent_level = 0):
        # first line
        current_indent_level = min_indent_level
        res = current_indent_level * tab + self.description + "\n"

        # following lines
        current_indent_level += 1
        for s in self.children:
            res += s.to_string(current_indent_level)

        return res

