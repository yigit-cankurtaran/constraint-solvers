# from z3 import Int, If, simplify
from z3 import *

x = Int("x")
y = Int("y")
max = If(x > y, x, y)

print(max)

simplify(max)  # simplify changed nothing here, nothing simpler than this
print(max)
