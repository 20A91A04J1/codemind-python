n=int(input())
a=list(map(int,input().split()))
b=a[0]
for i in a:
    if b>i:
        b=i
print(i)