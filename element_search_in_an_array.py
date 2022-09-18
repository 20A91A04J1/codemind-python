n=int(input())
a=list(map(int,input().split()))
b=int(input())
s=0
for i in a:
    if b==i:
        s+=1
        break
if s==1:print("True")
else:print("False")