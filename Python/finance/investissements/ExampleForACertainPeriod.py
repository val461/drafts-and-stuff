#!/usr/bin/env python3


import math
from decimal import Decimal


def GCD(a, b):
    assert a > 0
    assert b > 0
    a, b = map(Decimal, (a, b))
    while b != 0:
        a, b = b, a % b
    return float(a)


class ExampleForACertainPeriod:

    def __init__(self, saved_per_month, duration_in_months, opening_balance, withdrawal_fees, portfolio_wanted_percentages, portfolio_return_rates_per_year, rebalance_period_in_months, fees_rate_per_year, fee_by_contribution, period_size_in_months, tick = None, account_type = None):

        self.desc = None
        self.duration_in_months = duration_in_months
        self.duration_in_years = duration_in_months / 12
        self.period_size_in_months = period_size_in_months
        self.opening_balance = opening_balance
        self.fee_by_contribution = fee_by_contribution
        self.account_type = account_type
        self.fees_rate_per_year = fees_rate_per_year
        self.withdrawal_fees = withdrawal_fees
        self.saved_per_month = saved_per_month
        self.portfolio_wanted_percentages = portfolio_wanted_percentages
        self.portfolio_return_rates_per_year = portfolio_return_rates_per_year
        self.rebalance_period_in_months = rebalance_period_in_months

        if tick:
            self.tick = tick
        elif self.rebalance_period_in_months:
            self.tick = GCD(self.period_size_in_months, self.rebalance_period_in_months)
        else:
            self.tick = self.period_size_in_months

        self.tick_in_years = self.tick / 12
        self.duration_in_periods = duration_in_months / self.period_size_in_months
        self.number_of_complete_periods = math.floor(self.duration_in_periods)
        self.recurrent_contribution = saved_per_month * self.period_size_in_months

        self.portfolio_return_factors_per_tick = [(1 + (return_rate_per_year - self.fees_rate_per_year) / 100) ** self.tick_in_years for return_rate_per_year in portfolio_return_rates_per_year]

        self.balance = opening_balance
        self.balances = [p / 100 * opening_balance for p in portfolio_wanted_percentages]
        self.rebalancing_fees = 0
        # print()
        # print()
        # print(' '.join(f'{b:7.2f}' for b in self.balances))
        recurrent_net_contribution = self.recurrent_contribution - fee_by_contribution
        months_since_last_rebalance = self.tick
        months_since_last_contribution = self.tick
        month_counter = self.tick
        while month_counter <= self.duration_in_months:
            for i in range(len(self.balances)):
                # returns
                self.balances[i] = self.balances[i] * self.portfolio_return_factors_per_tick[i]
            if self.rebalance_period_in_months and months_since_last_rebalance >= self.rebalance_period_in_months:
                # rebalancing
                # print('rebalancing')
                self.balance = sum(self.balances)
                # print(' '.join(f'{self.balances[i] / self.balance * 100:4.1f}' for i in range(len(self.balances))))
                # print(' '.join(f'{b:7.2f}' for b in self.balances))
                self.balance = sum(self.balances) - fee_by_contribution * len(self.balances)
                for i in range(len(self.balances)):
                    self.balances[i] = portfolio_wanted_percentages[i] / 100 * self.balance
                # print(' '.join(f'{self.balances[i] / self.balance * 100:4.1f}' for i in range(len(self.balances))))
                # print(' '.join(f'{b:7.2f}' for b in self.balances))
                self.rebalancing_fees += fee_by_contribution * len(self.balances)
                months_since_last_rebalance = 0
            if months_since_last_contribution >= self.period_size_in_months:
                # contribution 
                for i in range(len(self.balances)):
                    self.balances[i] += portfolio_wanted_percentages[i] / 100 * recurrent_net_contribution
                months_since_last_contribution = 0
            month_counter += self.tick
            months_since_last_contribution += self.tick
            months_since_last_rebalance += self.tick
            # print(f'month_counter {month_counter} '+' '.join(f'{b:7.2f}' for b in self.balances))
        # print()
        self.balance = sum(self.balances)

        self.contributions = self.recurrent_contribution * self.number_of_complete_periods
        self.not_a_divisor = self.contributions < saved_per_month * duration_in_months
        self.contribution_fees = fee_by_contribution * self.number_of_complete_periods
        self.fees_except_rebalancing_fees = self.contribution_fees + self.withdrawal_fees
        self.invested = opening_balance + self.contributions - self.contribution_fees
        self.returns = self.balance - self.invested

        self.net = self.returns - self.fees_except_rebalancing_fees
        if not self.account_type:
            self.total_return_rate = self.net / self.invested * 100
            self.annualized = ((1 + self.total_return_rate / 100) ** (1 / self.duration_in_years) - 1) * 100
        elif self.account_type == 'PEA':
            # post tax PEA after at least 5 years
            # assert self.duration_in_years >= 5
            # if self.duration_in_years < 5:
                # print('warning: duration smaller than 5 years, so PEA taxes may be understimated')
            self.net = self.returns * (100 - 17.2) / 100 - self.fees_except_rebalancing_fees
            self.total_return_rate = self.net / self.invested * 100
            self.annualized = ((1 + self.total_return_rate / 100) ** (1 / self.duration_in_years) - 1) * 100
        else:
            assert self.account_type == 'AV'
            # post tax assurance vie after at least 8 years
            # assert self.duration_in_years >= 8
            # if self.duration_in_years < 8:
                # print('warning: duration smaller than 8 years, so AV taxes may be understimated')
            if self.returns <= 4600:
                self.net = self.returns * (100 - 17.2) / 100 - self.fees_except_rebalancing_fees
            else:
                # very roughly
                self.net = self.returns * (100 - 17.2 - 7.5) / 100 - self.fees_except_rebalancing_fees
            self.total_return_rate = self.net / self.invested * 100
            self.annualized = ((1 + self.total_return_rate / 100) ** (1 / self.duration_in_years) - 1) * 100


    def __str__(self):
        if not self.desc:
            type_string = ''
            divisor_string = ''
            rebalancing_string = ''
            if self.account_type:
                type_string = f'{self.account_type}: '
            if self.not_a_divisor:
                divisor_string = f', contributions {self.contributions}'
            if self.rebalance_period_in_months:
                rebalancing_string = f', rebalance every {self.rebalance_period_in_months:2} month(s)'

            self.desc = f'{type_string}{self.recurrent_contribution:6.1f} contributed every {self.period_size_in_months:4} month(s){rebalancing_string}, net {self.net:7.2f}, annualized {self.annualized:5.2f} %, total {self.total_return_rate:.2f} %, returns {self.returns:7.2f}, total fees {self.fees_except_rebalancing_fees + self.rebalancing_fees:6.2f}, end balance {self.balance:.2f}, invested {self.invested:.0f}, end balance - fees {self.balance - self.fees_except_rebalancing_fees:.2f}{divisor_string}'

        return self.desc


    def __repr__(self):
        attributes = [a.split(' = ')[0] for a in 'saved_per_month, duration_in_months, opening_balance, withdrawal_fees, portfolio_wanted_percentages, portfolio_return_rates_per_year, rebalance_period_in_months, fees_rate_per_year, fee_by_contribution, period_size_in_months, tick = None, account_type = None'.split(', ')]
        s = ', '.join([f'{attribute} = {getattr(self, attribute)!r}' for attribute in attributes])
        return f'ExampleForACertainPeriod({s})'
