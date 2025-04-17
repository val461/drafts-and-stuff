# https://chatgpt.com/c/68014a7a-1194-800a-9c59-f480abe6bfbf

import random
import numpy as np
import time
import threading

# Distributions
def rand_uniform(a=-10, b=10):
    return random.uniform(a, b)

def rand_normal(mu=0, sigma=3):
    return random.gauss(mu, sigma)

def rand_poisson(lam=3):
    return np.random.poisson(lam)

def rand_choice(options):
    return random.choice(options)

def rand_value():
    dist = rand_choice(['uniform', 'normal', 'poisson', 'bool', 'int'])
    if dist == 'uniform':
        return rand_uniform()
    elif dist == 'normal':
        return rand_normal()
    elif dist == 'poisson':
        return rand_poisson()
    elif dist == 'bool':
        return rand_choice([True, False])
    elif dist == 'int':
        return random.randint(-100, 100)

class RandVar:
    def __init__(self, name):
        self.name = name
        self.value = rand_value()
        self.start_mutation()

    def assign(self):
        self.value = rand_value()

    def mutate(self):
        while True:
            time.sleep(random.uniform(1, 5))  # mutation interval
            old_value = self.value
            self.value = rand_value()
            print(f"[MUTATION] {self.name} changed from {old_value} to {self.value}")

    def start_mutation(self):
        thread = threading.Thread(target=self.mutate, daemon=True)
        thread.start()

    def __repr__(self):
        return f"{self.value}"

# Example program
x = RandVar("x")
y = RandVar("y")

print(f"Initial x = {x}")
print(f"Initial y = {y}")

time.sleep(2)
print("Manually reassigning x := ??")
x.assign()
print(f"Now x = {x}")

print("Letting chaos take over for 10 seconds...")
time.sleep(10)
