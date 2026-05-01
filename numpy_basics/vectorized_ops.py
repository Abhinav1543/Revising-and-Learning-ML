import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

result = a+b
comp = a > b
x = np.sqrt(a)
l = np.log(b)

print(f"""Plus : {result}
Comparision : {comp}
Square Root : {x}
Log values : {l}""")