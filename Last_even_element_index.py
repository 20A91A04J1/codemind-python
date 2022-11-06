n=int(input())
a=list(map(int,input().split()))
s=0
for j in range (n):
    if a[j]%2==0:
        s=j
print(s)