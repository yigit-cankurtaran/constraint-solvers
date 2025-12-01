from z3 import Int, Optimize

"""exercise: integers x, y
x + y = 12
x * y is MAXIMIZED (switch to Optimize)
x, y ∈ [0, 12]"""

x = Int("x")
y = Int("y")

o = Optimize()

o.add(x + y == 12)
o.add(x >= 0, x <= 12, y >= 0, y <= 12)
# h = o.maximize(x * y) # part of solution
h = o.minimize(x * y)

print(o.check())
print(o.model())
