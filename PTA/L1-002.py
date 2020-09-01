import math

N, x = input("").split()
N = int(N)

n = int(math.sqrt((N + 1) / 2))
s_1 = 0
s_2 = 0

for i in range(0, 2 * n - 1):
    if i < n:
        s_1 += (2 * (n - i) - 1)
        print(i * " " + (2 * (n - i) - 1) * x)
    else:
        s_2 += (2 * (i - n) + 3)
        print((2 * n - 2 - i) * " " + (2 * (i - n) + 3) * x)
        
sum = s_1 + s_2
s = N - sum
print(s)
