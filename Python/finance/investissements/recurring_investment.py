#!/usr/bin/env python3


from ExampleForACertainPeriod import ExampleForACertainPeriod, GCD


def divisors_of(n):
    assert n >= 1
    return [d for d in range(1, n + 1) if n % d == 0]


# Parameters


# account_type = None
# account_type = 'PEA'
account_type = 'AV'
saved_per_month = 25            # currency amount
# saved_per_month = 0            # currency amount
duration_in_months = 12*8
# duration_in_months = 12
opening_balance = 2600          # currency amount
# opening_balance = 100          # currency amount


# I think in this simulator, you should stick to a single product in the portfolio.
# Indeed, without rebalancing, using several products in the portfolio is likely to lead to an unbalanced portfolio.

# percentages
portfolio_wanted_percentages = [100]
portfolio_return_rates_per_year = [15.31]
# portfolio_wanted_percentages = [90, 10]
# portfolio_return_rates_per_year = [10, 3]

# period_sizes_to_try = [0.5] + list(range(1, 25))    # in months
# period_sizes_to_try = [x for x in (0.25 * i for i in range(1, 12)) if duration_in_months % x == 0]    # in months
# period_sizes_to_try = [12]    # in months
period_sizes_to_try = [0.25, 0.5] + divisors_of(duration_in_months)    # in months
# period_sizes_to_try = divisors_of(duration_in_months)    # in months


# This simulator seems too unrealistic for the rebalancing simulation to be useful.

rebalance_periods_to_try = [None]   # do not simulate rebalancing
# rebalance_periods_to_try = list(range(1, 14))    # in months
# rebalance_periods_to_try = list(range(1, 14)) + [15, 18, 24, 36, 72, 100]    # in months
# rebalance_periods_to_try = [1, 3, 6, 12]    # in months

tick = None

# show_plot = False
show_plot = True

x_axis = period_sizes_to_try
# x_axis = rebalance_periods_to_try

show_many_examples = True
# show_many_examples = False

fees_rate_per_year_PEA = 0          # percentage for PEA
# fee_by_contribution_PEA = 1      # currency amount for PEA
fee_by_contribution_PEA = 0      # currency amount for PEA
# withdrawal_fees_PEA = 6             # currency amount
withdrawal_fees_PEA = 0             # currency amount
# withdrawal_fees_PEA = 6+4*4*duration_in_months/12*fee_by_contribution_PEA             # currency amount

fees_rate_per_year_AV = 0.6       # percentage for AV
# fee_by_contribution_AV = 0         # currency amount for AV
fee_by_contribution_AV = '0.1 %'         # currency amount for AV   TODO
# withdrawal_fees_AV = 6             # currency amount
withdrawal_fees_AV = 0             # currency amount

if not account_type:
    fees_rate_per_year = 0          # percentage
    fee_by_contribution = 0.99      # currency amount
    withdrawal_fees = 6             # currency amount
elif account_type == 'PEA':
    fees_rate_per_year = fees_rate_per_year_PEA
    fee_by_contribution = fee_by_contribution_PEA
    withdrawal_fees = withdrawal_fees_PEA
else:
    assert account_type == 'AV'
    fees_rate_per_year = fees_rate_per_year_AV
    fee_by_contribution = fee_by_contribution_AV
    withdrawal_fees = withdrawal_fees_AV


# Code

print(f'expected total contributions (including fees) {saved_per_month * duration_in_months}\n')
# (normally, amount reached when period size is a divisor of the total duration)

if show_many_examples:
    examples = []
    for period_size_in_months in period_sizes_to_try:
        for rebalance_period_in_months in rebalance_periods_to_try:
            examples.append(ExampleForACertainPeriod(saved_per_month, duration_in_months, opening_balance, withdrawal_fees, portfolio_wanted_percentages, portfolio_return_rates_per_year, rebalance_period_in_months, fees_rate_per_year, fee_by_contribution, period_size_in_months, tick, account_type))
            print(examples[-1])

    # best = max(examples, key = lambda example: example.net)
    best = max(examples, key = lambda example: example.net)
    print(f'\nbest:\n\n{best}\n\nrepr: {best.__repr__()}')

    if show_plot:
        import matplotlib.pyplot as plt
        plt.plot(x_axis, [x.net for x in examples])
        plt.show()
else:
    # chosen_example_for_PEA = ExampleForACertainPeriod(saved_per_month, duration_in_months, opening_balance, withdrawal_fees, portfolio_wanted_percentages, portfolio_return_rates_per_year, rebalance_period_in_months, fees_rate_per_year = fees_rate_per_year_PEA, fee_by_contribution = fee_by_contribution_PEA, period_size_in_months = 3, tick = tick, account_type = 'PEA')

    chosen_example_for_PEA = ExampleForACertainPeriod(saved_per_month = 25, duration_in_months = 96, opening_balance = 2600, withdrawal_fees = 0, portfolio_wanted_percentages = [100], portfolio_return_rates_per_year = [15.31], rebalance_period_in_months = None, fees_rate_per_year = 0, fee_by_contribution = 0, period_size_in_months = 0.25, tick = 0.25, account_type = 'PEA')

    chosen_example_for_AV = ExampleForACertainPeriod(saved_per_month, duration_in_months, opening_balance, withdrawal_fees, portfolio_wanted_percentages, portfolio_return_rates_per_year, rebalance_period_in_months, fees_rate_per_year = fees_rate_per_year_AV, fee_by_contribution = fee_by_contribution_AV, period_size_in_months = 0.25, tick = tick, account_type = 'AV')

    print(chosen_example_for_PEA)
    print(chosen_example_for_AV)
