from functools import partial
from typing import Callable

"""
def multiply(x, y, z):
    return x * y * z

double_and_multiply = partial(multiply, 2)

result = double_and_multiply(3, 4)

print(result)  # output: 24
"""

class Calculator:
  def calculate(self, a, b, c):
    return a * b * c

class MathAgent:
  def __init__(self, calc_func: Callable[[int, int], int] = None):
    if calc_func is None:
        # default calc_func is Calculator().calculate(2, b, c)
      self.calc_func = partial(Calculator().calculate, 2)
    else:
      self.calc_func = calc_func

  def run(self, b, c):
    return self.calc_func(b, c)

# use default calc_func
agent = MathAgent()
print(agent.run(3, 4))  # output: 24, equivalent to Calculator().calculate(2, 3, 4)

# provide custom calc_func
custom_calc_func = partial(Calculator().calculate, 3)
agent_with_custom_func = MathAgent(calc_func=custom_calc_func)
print(agent_with_custom_func.run(3, 4))  # output: 36, equivalent to Calculator().calculate(3, 3, 4)
