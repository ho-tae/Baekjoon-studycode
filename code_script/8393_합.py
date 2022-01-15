n = int(input())
a =[]
for i in range(n):
    a.append(i+1)
print(sum(a))

# 다른 방법 1
n = int(input())
print(n*(n+1)/2)

# 다른 방법 2
n = int(input())
print(sum(range(1,n+1)))
