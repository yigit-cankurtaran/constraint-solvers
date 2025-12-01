from z3 import Int, Solver

x = Int("x")
y = Int("y")

s = Solver()
s.add(x + y == 10)
s.add(x > y)

print(s.check())  # prints "sat"
print(s.model())  # prints [y = 4, x = 6]
