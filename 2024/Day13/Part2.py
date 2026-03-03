import re, z3

from z3 import Z3Exception
from Util.util import read_input

data = read_input(13, True)
result = 0

for i in range(0,len(data),4):
    match_a = list(map(int, re.findall(r"\d+", data[i])))
    match_b = list(map(int, re.findall(r"\d+", data[i + 1])))
    match_c = list(map(int, re.findall(r"\d+", data[i + 2])))

    matrix_solver = z3.Optimize()
    var1 = z3.Int("A")
    var2 = z3.Int("B")
    matrix_solver.add(var1 >= 0)
    matrix_solver.add(var2 >= 0)

    A =  [match_a[0], match_b[0]]
    B = [match_a[1], match_b[1]]
    prize = [match_c[0] + 10000000000000, match_c[1] + 10000000000000]

    equation = A[0] * var1 + A[1] * var2
    matrix_solver.add(equation == prize[0])
    equation = B[0] * var1 + B[1] * var2
    matrix_solver.add(equation == prize[1])
    matrix_solver.minimize(var1 + var2)
    matrix_solver.check()

    try:
       result += matrix_solver.model().eval(3 * var1 + var2).as_long()
    except Z3Exception:
        result += 0


print(result)