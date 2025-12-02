# from z3 import Int, If, simplify
from z3 import *

x = Int("x")
y = Int("y")
max = If(x > y, x, y)

print(f"max is {max}")

max_simplified = simplify(max)
print(f"max simplified is {max_simplified}")
