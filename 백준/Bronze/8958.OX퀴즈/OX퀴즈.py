b = int(input())
for i in range(b):
    c = 1
    a = input()
    s = list(a)
    sum = 0
    for j in s:
        if j == "O":
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
            