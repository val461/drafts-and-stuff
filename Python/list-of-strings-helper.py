#!/usr/bin/env python3

# Rather than this script, consider using str.split().

# Usage:
# for the clipboard feature:    python -i list-of-strings-helper.py
# otherwise:                    ./list-of-strings-helper.py

# Example:
#   input: 'account, currency, amount, cleared, comment'
#   output: 'account', 'currency', 'amount', 'cleared', 'comment'

import clipboard

# sentence = input('Words: ')
sentence = 'account, currency, amount, cleared, comment'
separator = ', '
quote = "'"
# quote = '"'

result = quote + f"{quote}, {quote}".join(sentence.split(separator)) + quote
print(result)
clipboard.copy(result)
print('(Copied to clipboard until the Python interpreter exits.)')
