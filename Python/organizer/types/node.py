#!/usr/bin/env python3

class Node:
    tab = 4 * " "

    def __init__(self, description="", children=[]):
        self.description = description
        self.children = children

    def to_string(self, min_indent_level=0):
        # first line
        current_indent_level = min_indent_level
        res = current_indent_level * tab + self.description + "\n"    # todo: use strftime(format) instead

        # following lines
        current_indent_level += 1
        for s in self.subtasks:
            res += s.to_string(current_indent_level)

        return res

#~ if __name__ == "__main__":
    #~ pass
