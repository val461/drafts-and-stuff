#!/usr/bin/env python3


import math, time


def chrono(duration = 1, quiet = False, separator = ' '):
    '''duration: in seconds.'''
    if quiet:
        time.sleep(duration)
    else:
        floor = math.floor(duration)
        fractional = duration - floor
        if fractional > 0:
            print(duration, end = separator, flush = True)
            time.sleep(fractional)
        for remaining in range(floor, 0, -1):
            print(remaining, end = separator, flush = True)
            time.sleep(1)
        print()
        # print(0)


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


    def __str__(self, verbose = False):
        if verbose:
            return f'{self.name} (hold {self.hold_duration}, rest {self.rest_duration}, repeat {self.repetitions})'
        else:
            return f'{self.name}\t(H {self.hold_duration:2},  R {self.rest_duration:2},  T {self.repetitions:2})'

    def __repr__(self):
        return f'{type(self).__name__}(hold_duration = {self.hold_duration}, rest_duration = {self.rest_duration}, repetitions = {self.repetitions}, hold_increment = {self.hold_increment}, rest_increment = {self.rest_increment}, repetitions_increment = {self.repetitions_increment}, name = {self.name.__repr__()})'

    def perform(self):
        print(f'\nNext exercise: {self}.\nReady? [enter]')
        input()
        for r in range(1, self.repetitions + 1):
            print(f'Hold.')
            chrono(self.hold_duration)
            print('Rest.')
            chrono(self.rest_duration)


    def increase_difficulty(self):
        self._change_difficulty(self.repetitions_increment)


    def decrease_difficulty(self):
        self._change_difficulty(-self.repetitions_increment)


    def _change_difficulty(self, difference):
        print(f'Previous:\t{self}.')
        new = self.repetitions + difference
        if new > 0:
            self.repetitions = new
        else:
            print(f'Did not decrease (too low).')
        print(f'New:\t\t{self}.')


class Quick(Exercise):

    def __init__(self, hold_duration = 1, rest_duration = 1, repetitions = 10, *args, **kw_args):
        super().__init__(hold_duration = hold_duration, rest_duration = rest_duration, repetitions = repetitions, *args, **kw_args)

    def perform(self):
        print(f'\nNext exercise: {self}.\nYou are supposed to press <enter> each time you release.\nReady? [enter]')
        input()
        for r in range(1, self.repetitions + 1):
            print(f'Hold and release.')
            input()


class Medium(Exercise):

    def __init__(self, hold_duration = 4, rest_duration = 2, repetitions = 5, *args, **kw_args):
        super().__init__(hold_duration = hold_duration, rest_duration = rest_duration, repetitions = repetitions, *args, **kw_args)


class Long(Exercise):

    def __init__(self, hold_duration = 10, rest_duration = 5, repetitions = 5, hold_increment = 2, rest_increment = 1, *args, **kw_args):
        super().__init__(hold_duration = hold_duration, rest_duration = rest_duration, repetitions = repetitions, hold_increment = hold_increment, rest_increment = rest_increment, *args, **kw_args)


    def increase_difficulty(self):
        print(f'Previous:\t{self}.')
        if self.hold_duration < 20:
            self.hold_duration += self.hold_increment
            self.rest_duration += self.rest_increment
        else:
            print(f'Did not increase (too high).')
        print(f'New:\t\t{self}.')


    def decrease_difficulty(self):
        print(f'Previous:\t{self}.')
        new_hold = self.hold_duration - self.hold_increment
        new_rest = self.rest_duration - self.rest_increment
        if new_hold > 0 and new_rest > 0:
            self.hold_duration = new_hold
            self.rest_duration = new_rest
        else:
            print(f'Did not decrease (too low).')
        print(f'New:\t\t{self}.')


    _change_difficulty = None


class Session:

    def __init__(self, load_from_file = False, filename = None):
        self.exercises = None
        self.filename = filename
        if load_from_file:
            self.exercises = self.load(filename)
        if not self.exercises:
            self.exercises = [Medium(), Quick(), Long()]


    def __str__(self):
        return '\n'.join(exercise.__str__() for exercise in self.exercises)


    def __repr__(self):
        return '\n'.join(exercise.__repr__() for exercise in self.exercises)


    # testme
    def load(self, filename = None):
        exercises = None
        if not filename:
            filename = self.filename
        if not filename:
            print('Error: filename not specified.')
        else:
            try:
                with open(filename, 'r') as my_file:
                    exercises = map(eval, my_file.readlines())
            except OSError as error:
                print(f'Error: failed to load file " {filename} ". ({error}.)')
        return exercises


    # testme
    def save(self, filename = None):
        done = False
        if not filename:
            filename = self.filename
        if not filename:
            print('Error: filename not specified.')
        else:
            try:
                with open(filename, 'w') as my_file:
                    my_file.write(self.__repr__()+'\n')
                    done = True
                    print(f'Saved to file {filename}.')
            except OSError as error:
                print(f'Error: failed to save to file " {filename} ". ({error})')
        return done


    def run(self):
        print(self)
        for exercise in self.exercises:
            exercise.perform()
            print('[i]ncrease / [d]ecrease difficulty? (Or <enter> to make no changes.)')
            answer = input().lower()
            if answer == 'i':
                exercise.increase_difficulty()
            elif answer == 'd':
                exercise.decrease_difficulty()
        print(self)
        print('Save? [y]/n')
        answer = input().lower()
        if answer == 'n':
            print('Not saving.')
        else:
            print('Saving.')
            self.save()


if __name__ == '__main__':
    s = Session(load_from_file = True, filename = 'K_data')
    # s = Session(filename = 'K_data')
    # s.save()
    s.run()
