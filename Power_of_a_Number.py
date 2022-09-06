x,y,m=map(int,input().split())
if 1<=x<=20 and 1<=y<=100 and 2<=m<=100:
    a=x**y%m
print(a)