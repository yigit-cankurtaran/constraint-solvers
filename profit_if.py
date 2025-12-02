from z3 import Int, If, simplify, Solver

income = Int("income")
loss = Int("loss")

profit = If(income - loss > 0, income - loss, loss - income)
print(f"profit is {profit}")

profit_simplified = simplify(profit)
print(f"profit simplified is {profit_simplified}")

s = Solver()
s.add(income + loss == 20000)
