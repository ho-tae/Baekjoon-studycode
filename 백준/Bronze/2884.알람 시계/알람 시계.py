h,m = map(int, input().split())
if h!=0 and 45<=m<60:
    print(h,m-45)
elif h!=0 and 0<=m<45:  # 10시 30분 -> 9시 45분
    print(h-1,60-(45-m))
elif h==0 and 45<=m<60: # 0시 30분 -> 23시 45분
    print(h,m-45)
else:
    print(23,60-(45-m))