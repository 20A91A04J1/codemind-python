a=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    b=int(int(i)**0.5)
    c=b*b
    if c==int(i):
        s+=int(i)
print(s)