from z3 import Int, If, simplify, Solver

income = Int("income")
loss = Int("loss")

profit = If(income - loss > 0, income - loss, loss - income)
print(f"profit is {profit}")

profit_simplified = simplify(profit)
print(f"profit simplified is {profit_simplified}")

s = Solver()
s.add(income == 10, loss == 7)
s.push()
s.add(profit != 3)  # trying to contradict expected val
print(s.check())  # returns unsat
s.pop()

s.push()
s.add(profit >= 3)
print(s.check())  # returns sat as well
print(s.model().evaluate(profit))  # prints 3
s.pop()
# push and pop works! constraint context is basically a stack machine
# check always checks the whole stack, we can use push and pop to look at individual constraints
# tbh i have no idea why we would want to do that but knowing it's a stack is helpful

# model evaluate = given all constraints and assignments, return value of expression
