#!/usr/bin/env python3

from node import Node
import datetime as d

class Task:
# todo class Task(Node):
    def __init__(self, description="", duration=d.timedelta(), start=d.datetime.now(), subtasks=[]):
        self.description = description
        self.duration = duration
        self.start = start
        self.subtasks = subtasks

    def actualizeDuration(self):
        if subtasks:
            self.duration = sum(map(getDuration, self.subtasks))

    def to_string(self, min_indent_level=0):
        # first line
        current_indent_level = min_indent_level
        res = current_indent_level * tab + self.start.isoformat() + "\n"    # todo: use strftime(format) instead

        # second line
        current_indent_level += 1
        res += current_indent_level * tab + self.description
        self.actualizeDuration()
        if self.duration != None:
            res += " ({})".format(self.duration)    # todo: use something like strftime(format) instead
        res += "\n"

        # following lines
        current_indent_level += 1
        for s in self.subtasks:
            res += s.to_string(current_indent_level)

        return res

#~ if __name__ == "__main__":
    #~ pass
