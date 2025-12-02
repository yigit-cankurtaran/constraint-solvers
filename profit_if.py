from z3 import Int, If, simplify, Solver

income = Int("income")
loss = Int("loss")

profit = If(income - loss > 0, income - loss, loss - income)
print(f"profit is {profit}")

profit_simplified = simplify(profit)
print(f"profit simplified is {profit_simplified}")

s = Solver()
s.add(income == 10, loss == 7)
s.add(profit != 3)  # trying to contradict expected val

print(s.check())  # returns unsat
