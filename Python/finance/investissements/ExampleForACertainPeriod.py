#!/usr/bin/env python3


import math


class ExampleForACertainPeriod:

    def __init__(self, return_rate_per_year, saved_per_month, duration_in_months, opening_balance, fees_rate_per_year, fee_by_contribution, period_size_in_months, account_type = None):

        self.desc = None
        self.duration_in_months = duration_in_months
        self.duration_in_years = duration_in_months / 12
        self.period_size_in_months = period_size_in_months
        self.opening_balance = opening_balance
        self.fee_by_contribution = fee_by_contribution
        self.account_type = account_type
        self.return_rate_per_year = return_rate_per_year - fees_rate_per_year
        self.whole_return_rate_per_year = return_rate_per_year
        self.fees_rate_per_year = fees_rate_per_year

        self.return_factor_per_period = (1 + self.return_rate_per_year / 100) ** (self.period_size_in_months / 12)
        self.duration_in_periods = duration_in_months / self.period_size_in_months
        self.number_of_complete_periods = math.floor(self.duration_in_periods)
        self.recurrent_contribution = saved_per_month * self.period_size_in_months

        self.balance = opening_balance
        for _ in range(self.number_of_complete_periods):
            self.balance = self.balance * self.return_factor_per_period + self.recurrent_contribution - fee_by_contribution

        self.contributions = self.recurrent_contribution * self.number_of_complete_periods
        self.fees = fee_by_contribution * self.number_of_complete_periods
        self.invested = opening_balance + self.contributions - self.fees
        self.returns = self.balance - self.invested
        self.net = self.returns - self.fees
        self.total_return_rate = self.net / self.invested * 100
        self.annualized = ((1 + self.total_return_rate / 100) ** (1 / self.duration_in_years) - 1) * 100

        # post tax PEA after at least 5 years
        self.net_post_tax_PEA = self.net * (100 - 17.2) / 100
        self.total_return_rate_post_tax_PEA = self.net_post_tax_PEA / self.invested * 100
        self.annualized_post_tax_PEA = ((1 + self.total_return_rate_post_tax_PEA / 100) ** (1 / self.duration_in_years) - 1) * 100

        # post tax assurance vie after at least 8 years and if net <= 4600 €
        self.net_post_tax_AV = self.net * (100 - 17.2) / 100
        self.total_return_rate_post_tax_AV = self.net_post_tax_AV / self.invested * 100
        self.annualized_post_tax_AV = ((1 + self.total_return_rate_post_tax_AV / 100) ** (1 / self.duration_in_years) - 1) * 100
        

 
    def __str__(self):
        if not self.desc:
            if self.account_type == None:
                self.desc = f'{self.recurrent_contribution:6.1f} contributed every {self.period_size_in_months:4} month(s), net {self.net:7.2f}, annualized {self.annualized:.2f} %, total {self.total_return_rate:.2f} %, returns {self.returns:7.2f}, total fees {self.fees:6.2f}, end balance {self.balance:.2f}, invested {self.invested:.0f}, end balance - fees {self.balance - self.fees:.2f}'
            elif self.account_type == 'PEA':
                self.desc = f'PEA: {self.recurrent_contribution:6.1f} contributed every {self.period_size_in_months:4} month(s), net {self.net_post_tax_PEA:7.2f}, annualized {self.annualized_post_tax_PEA:.2f} %, total {self.total_return_rate_post_tax_PEA:.2f} %, returns {self.returns:7.2f}, total fees {self.fees:6.2f}, end balance {self.balance:.2f}, invested {self.invested:.0f}, contributions {self.contributions:.2f}'
            else:
                assert(self.account_type == 'AV')
                self.desc = f' AV: {self.recurrent_contribution:6.1f} contributed every {self.period_size_in_months:4} month(s), net {self.net_post_tax_AV:7.2f}, annualized {self.annualized_post_tax_AV:.2f} %, total {self.total_return_rate_post_tax_AV:.2f} %, returns {self.returns:7.2f}, total fees {self.fees:6.2f}, end balance {self.balance:.2f}, invested {self.invested:.0f}, contributions {self.contributions:.2f}'
        return self.desc
