n=int(input())      #175
c=str(n)
s=0
for i in c:
    t=int(i)**int(c.index(i)+1)
    s+=t
if s==n:
    print("True")
else:print("False")