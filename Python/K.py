#!/usr/bin/env python3


import math, time


def chrono(duration = 1, quiet = False, separator = ' '):
    '''duration: in seconds.'''
    if quiet:
        time.sleep(duration)
    else:
        for remaining in range(duration, 0, -1):
            print(remaining, end = separator, flush = True)
            time.sleep(1)
        print(0)


class Exercise:

    def __init__(self, hold_duration = 1, rest_duration = 1, repetitions = 1, hold_increment = 1, rest_increment = 1, repetitions_increment = 1, name = None):
        self.hold_duration = hold_duration
        self.rest_duration = rest_duration
        self.repetitions = repetitions
        self.hold_increment = hold_increment
        self.rest_increment = rest_increment
        self.repetitions_increment = repetitions_increment
        if name:
            self.name = name
        else:
            self.name = type(self).__name__


    def increase_difficulty(self):
        print(f'Previous: {self}.')

        self.repetitions += self.repetitions_increment

        print(f'New: {self}.')


    def decrease_difficulty(self):
        print(f'Previous: {self}.')

        new = self.repetitions - self.repetitions_increment
        if new > 0:
            self.repetitions = new

        print(f'New: {self}.')


    def __str__(self, verbose = False):
        if verbose:
            return f'{self.name} (hold {self.hold_duration}, rest {self.rest_duration}, repeat {self.repetitions})'
        else:
            return f'{self.name}\t(H {self.hold_duration:2},  R {self.rest_duration:2},  T {self.repetitions:2})'

    def perform(self):
        print(f'\nNext exercise: {self}.\nReady? [enter]')
        input()
        for r in range(1, self.repetitions + 1):
            print(f'Hold.')
            chrono(self.hold_duration)
            print('Rest.')
            chrono(self.rest_duration)


class Quick(Exercise):

    def __init__(self, hold_duration = 1, rest_duration = 1, repetitions = 10, *args, **kw_args):
        super().__init__(hold_duration = hold_duration, rest_duration = rest_duration, repetitions = repetitions, *args, **kw_args)

    def perform(self):
        print(f'\nNext exercise: {self}.\nYou will have to press <enter> each time you release.\nReady? [enter]')
        input()
        for r in range(1, self.repetitions + 1):
            print(f'Hold and release.')
            input()


class Medium(Exercise):

    def __init__(self, hold_duration = 4, rest_duration = 2, repetitions = 5, *args, **kw_args):
        super().__init__(hold_duration = hold_duration, rest_duration = rest_duration, repetitions = repetitions, *args, **kw_args)


class Long(Exercise):

    def __init__(self, hold_duration = 10, rest_duration = 5, repetitions = 5, *args, **kw_args):
        super().__init__(hold_duration = hold_duration, rest_duration = rest_duration, repetitions = repetitions, *args, **kw_args)


class Session:

    def __init__(self, load_from_file = False, filename = None):
        self.filename = filename
        if load_from_file:
            # todo
            data = load(filename)
            self.exercises = [Medium(), Quick(), Long()]
        else:
            self.exercises = [Medium(), Quick(), Long()]


    def __str__(self):
        return '\n'.join(map(str, self.exercises))


    def load(self, filename = None):
        if not filename:
            filename = self.filename
        data = None
        # todo
        return data


    def save(self, filename = None):
        if not filename:
            filename = self.filename
        # todo
        pass


    def run(self):
        print(self)
        # for exercise in self.exercises:
        for exercise in self.exercises:
            exercise.perform()
            print('[i]ncrease / [d]ecrease difficulty? (Or <enter> to make no changes.)')
            answer = input().lower()
            if answer == 'i':
                exercise.increase_difficulty()
            elif answer == 'd':
                exercise.decrease_difficulty()


if __name__ == '__main__':
    s = Session()
    s.run()
