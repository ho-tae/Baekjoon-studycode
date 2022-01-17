A, B, C = map(int, input())
D, E, F = map(int, input())
x = A*100 + B*10 + C
y = D*100 + E*10 + F
print(x*F)
print(x*E)
print(x*D)
print(x*D*100 + x*E*10 + x*F)