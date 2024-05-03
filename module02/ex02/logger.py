import os
import time
from random import randint
import functools

# Definition of log decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = os.getenv('USER')
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"({user})Running: {func.__name__}  [exec-time = {elapsed:.4f} ms]")
        return result
    return wrapper

class CoffeeMachine:
    def __init__(self):
        self.water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            print("Machine is starting.")
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "Boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            self.boil_water()
            print("Coffee made!")
        else:
            print("Cannot make coffee.")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub... New water level:", self.water_level)

if __name__ == "__main__":
    machine = CoffeeMachine()
    for _ in range(5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(50)
