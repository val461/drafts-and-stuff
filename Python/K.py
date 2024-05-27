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
        # print()
        print(0)


class Exercise:

    def __init__(self, hold_duration = 1, rest_duration = 1, repetitions = 1, hold_increment = 0, rest_increment = 0, repetitions_increment = 1, use_chrono = True, name = None):
        self.hold_duration = hold_duration
        self.rest_duration = rest_duration
        self.repetitions = int(repetitions)
        self.hold_increment = hold_increment
        self.rest_increment = rest_increment
        self.repetitions_increment = repetitions_increment
        self.use_chrono = use_chrono
        if name:
            self.name = name
        else:
            self.name = type(self).__name__


    @classmethod
    def new_from_template(cls, template):
        '''template: 'Quick', 'Medium', or 'Long'
        '''
        result = None
        if template == 'Quick':
            result = cls(hold_duration = 0.7, rest_duration = 0.5, repetitions = 10, hold_increment = 0, rest_increment = 0, repetitions_increment = 2, use_chrono = True, name = template)
        elif template == 'Medium':
            result = cls(hold_duration = 4, rest_duration = 2, repetitions = 5, hold_increment = 0, rest_increment = 0, repetitions_increment = 1, use_chrono = True, name = template)
        elif template == 'Long':
            result = cls(hold_duration = 10, rest_duration = 5, repetitions = 5, hold_increment = 1, rest_increment = 0.5, repetitions_increment = 0, use_chrono = True, name = template)
        else:
            raise ValueError
        return result


    def __str__(self, verbose = False):
        if verbose:
            return f'{self.name} (hold {self.hold_duration}, rest {self.rest_duration}, repeat {self.repetitions})'
        else:
            return f'{self.name}\t(H {self.hold_duration:2},  R {self.rest_duration:2},  T {self.repetitions:2})'


    def __repr__(self):
        return f'Exercise(hold_duration = {self.hold_duration}, rest_duration = {self.rest_duration}, repetitions = {self.repetitions}, hold_increment = {self.hold_increment}, rest_increment = {self.rest_increment}, repetitions_increment = {self.repetitions_increment}, use_chrono = {self.use_chrono}, name = {self.name.__repr__()})'


    def perform(self):
        print(f'\nNext exercise: {self}.\n')
        if self.use_chrono:
            print(f'Ready? [enter]')
            input()
            for r in range(1, self.repetitions + 1):
                print(f'Hold. ({r} / {self.repetitions})')
                chrono(self.hold_duration)
                print('Rest.')
                chrono(self.rest_duration)
        else:
            print(f'Press <enter> each time you release.\nReady? [enter]')
            input()
            for r in range(1, self.repetitions + 1):
                print(f'Hold and release. ({r} / {self.repetitions})')
                input()


    def increase_difficulty(self):
        self._change_difficulty(1)


    def decrease_difficulty(self):
        self._change_difficulty(-1)


    def _change_difficulty(self, factor = 1):
        '''factor: scales increment.'''
        print(f'Previous:\t{self}.')
        new_hold = self.hold_duration + factor * self.hold_increment
        new_rest = self.rest_duration + factor * self.rest_increment
        new_repetitions = int(self.repetitions + factor * self.repetitions_increment)
        if new_hold <= 0:
            print(f'Error: hold duration too low.')
        elif new_hold > 20:
            print(f'Error: hold duration too high.')
        elif new_rest <= 0:
            print(f'Error: rest duration too low.')
        elif new_repetitions <= 0:
            print(f'Error: repetitions too low.')
        else:
            self.hold_duration = new_hold
            self.rest_duration = new_rest
            self.repetitions = new_repetitions
        print(f'New:\t\t{self}.')


class Session:

    def __init__(self, load_from_file = False, filename = None):
        self.exercises = None
        self.filename = filename
        if load_from_file:
            self.exercises = self.load(filename)
        if not self.exercises:
            print('Using default exercises.\n')
            self.exercises = list(map(Exercise.new_from_template, ['Medium', 'Quick', 'Long']))


    def __str__(self):
        return '\n'.join(exercise.__str__() for exercise in self.exercises)


    def __repr__(self):
        return '\n'.join(exercise.__repr__() for exercise in self.exercises)


    def load(self, filename = None):
        exercises = None
        if not filename:
            filename = self.filename
        if not filename:
            print('Error: filename not specified.')
        else:
            try:
                with open(filename, 'r') as my_file:
                    exercises = list(map(eval, my_file.readlines()))
            except OSError as error:
                print(f'Warning: failed to load file " {filename} ". ({error}.)\n')
            else:
                print(f'Loaded exercises from {filename}.\n')
        return exercises


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
                print(f'Error: failed to save to file " {filename} ". ({error})\n')
        return done


    def run(self, ask = True):
        answer = None
        if ask:
            print('Perform? [y]/n')
            answer = input().lower()
        if answer == 'n':
            perform = False
        else:
            perform = True

        print(self)
        modified = False
        for exercise in self.exercises:
            if perform:
                exercise.perform()
            else:
                print(f'\nexercise: {exercise}.')
            if ask:
                print('[i]ncrease / [d]ecrease difficulty? (<enter> to make no changes.)')
                answer = input().lower()
                if answer == 'i':
                    exercise.increase_difficulty()
                    modified = True
                elif answer == 'd':
                    exercise.decrease_difficulty()
                    modified = True

        if ask:
            print()
            print(self)
            if self.filename:
                if modified:
                    print('Save? [y]/n')
                    answer = input().lower()
                    if answer == 'n':
                        print('Not saving.')
                    else:
                        self.save()
                else:
                    print('Save? y/[n]')
                    answer = input().lower()
                    if answer == 'y':
                        self.save()
                    else:
                        print('Not saving.')

if __name__ == '__main__':
    s = Session(load_from_file = True, filename = 'K_data')
    # s.run()
    s.run(ask = False)
