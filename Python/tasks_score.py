#!/usr/bin/env python3

def NOW():
    pass

class Challenge:
    '''Data attributes in this class are not meant to be accessed manually.'''

    def __init__(self, beginning = None, targeted_duration = 1 TIME_UNIT, earned_points_by_time_unit = 1):
        '''targeted_duration: positive
        earned_points_by_time_unit: positive or negative'''

        self._beginning = beginning if beginning else NOW()
        self._targeted_duration = targeted_duration
        self._earned_points_by_time_unit = earned_points_by_time_unit
        self._score = None
        self._actual_end = None

    def needs_to_be_closed(self):

        return (self._actual_end == None
            and NOW() >= self.get_targeted_end())

    def get_actual_duration(self):

        return self._actual_end - self._beginning

    def get_score(self):

        return self._score

    def get_stake(self):

        return self._targeted_duration * self._earned_points_by_time_unit

    def get_targeted_end(self):

        return self._beginning + self._targeted_duration

    def set_end(self, actual_end = None):
        '''Sets end date; determines score.'''

        if not actual_end:
            actual_end = NOW()

        self._actual_end = min(self.get_targeted_end(), actual_end)
        actual_duration = self.get_actual_duration()

        if actual_duration < self._targeted_duration:
            self._score = -self.get_stake() * ((self._targeted_duration - actual_duration) / self._targeted_duration)
        else:
            self._score = self.get_stake()

class Session:

    def __init__(self, data_file = './nofap.save', session_beginning = None, streak_beginning = None):

        now = NOW()
        self.data_file = data_file
        self.Load()

        if not self._score:
            self._score = 0

        if not self.session_beginning:
            self.session_beginning = session_beginning if session_beginning else now

        if not self.streak_beginning:
            self.streak_beginning = streak_beginning if streak_beginning else now

        if not self.challenge:
            self.challenge = None

    def Start_challenge(self, **args):

        self.Update()

        if self.challenge and self.challenge.was_closed():
            print("Error: a challenge is already ongoing.")
        else:
            self.challenge = Challenge(**args)

    def Close_challenge(self, date = None):

        if not date:
            date = NOW()

        self.challenge.set_end(date)
        self._score += self.challenge._score
        self.challenge = None

    def Reset_streak(self, date = None):

        if not date:
            date = NOW()

        self.streak_beginning = date

        if self.challenge and not self.challenge.was_closed():
            self.Close_challenge(date)

    def Update(self):

        if self.challenge and self.challenge.needs_to_be_closed():
            self.Close_challenge()

    def Load(self):

        pass
        # ~ READ(self.data_file)

    def Save(self):

        pass
        # ~ WRITE(self.ToJSON(), self.data_file)
