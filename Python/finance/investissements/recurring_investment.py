#!/usr/bin/env python3

from ExampleForACertainPeriod import ExampleForACertainPeriod


def divisors_of(n):
    assert(n >= 1)
    return [d for d in range(1, n + 1) if n % d == 0]


# Parameters


# account_type = None
account_type = 'PEA'
# account_type = 'AV'
saved_per_month = 25            # currency amount
duration_in_months = 12*8
return_rate_per_year = 10       # percentage
opening_balance = 1000          # currency amount    
# period_sizes_to_try = [0.5] + list(range(1, 25))    # in months
# period_sizes_to_try = [23]    # in months
period_sizes_to_try = [0.25, 0.5] + divisors_of(duration_in_months)    # in months
# period_sizes_to_try = [x for x in (0.25 * i for i in range(1, 12)) if duration_in_months % x == 0]    # in months
# all_periods_are_divisors_of_total_duration = False
all_periods_are_divisors_of_total_duration = True
show_plot = False
# show_plot = True

# just_the_final_examples = False
just_the_final_examples = True

if account_type == 'AV':
    fees_rate_per_year = 0.75       # percentage for AV
    fee_by_contribution = 0         # currency amount for AV
else:
    fees_rate_per_year = 0          # percentage for PEA
    fee_by_contribution = 0.99      # currency amount for PEA


# Code

print(f'maximal possible total contributions (including fees) {saved_per_month * duration_in_months}\n')
# (normally, amount reached only when period size is a divisor of the total duration)

if just_the_final_examples:
    chosen_example_for_PEA = ExampleForACertainPeriod(return_rate_per_year, saved_per_month, duration_in_months, opening_balance = 1000, fees_rate_per_year = 0, fee_by_contribution = 0.99, period_size_in_months = 3, account_type = 'PEA')
    chosen_example_for_AV = ExampleForACertainPeriod(return_rate_per_year, saved_per_month, duration_in_months, opening_balance = 1000, fees_rate_per_year = 0.75, fee_by_contribution = 0, period_size_in_months = 0.25, account_type = 'AV')
    print(chosen_example_for_PEA)
    print(chosen_example_for_AV)
else:
    examples = []
    for period_size_in_months in period_sizes_to_try:
        examples.append(ExampleForACertainPeriod(return_rate_per_year, saved_per_month, duration_in_months, opening_balance, fees_rate_per_year, fee_by_contribution, period_size_in_months, account_type))
        print(examples[-1])

    # best = max(examples, key = lambda example: example.net)
    best = max(examples, key = lambda example: example.net_post_tax_PEA)
    print(f'\nbest:\n\n{best}')

    if show_plot:
        import matplotlib.pyplot as plt
        plt.plot(period_sizes_to_try, [x.net for x in examples])
        plt.show()
