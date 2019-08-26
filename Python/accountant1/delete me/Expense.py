#!/usr/bin/env python3

class Transaction:

    def __init__(self, amount, account, description="", date, category):
        self.amount = amount
        self.description = description
        self.date = date
        self.category = category
