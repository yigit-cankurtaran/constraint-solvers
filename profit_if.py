from z3 import Int, If, simplify, Solver

income = Int("income")
loss = Int("loss")

profit = If(income - loss > 0, income - loss, -(loss - income))
print(f"profit is {profit}")

profit_simplified = simplify(profit)
print(f"profit simplified is {profit_simplified}")

s = Solver()
s.add(income == 10, loss == 7)
s.add(profit != 3)  # trying to contradict expected val

print(s.check())  # returns unsat

s.add(profit >= 3)
print(s.check())  # returns unsat as well
# the issue is, add ADDS constraints, doesn't write over the previous one
# we are adding another constraint on top of a wrong constraint.
# the first constraint will always be wrong, therefore both of our results
# will return "unsat"

a = Solver()  # new solver
a.add(income == 7, loss == 10)
a.add(profit < 0)
print(a.check())  # prints "sat"
print(a.model().evaluate(profit))  # prints "-3"
# this is how we get individual vars
# profit is symbolic, we need to ask the solver what it became
