c = []

for i in range(10):
    A = int(input())
    c.append(A%42)
c = set(c)
print(len(c))