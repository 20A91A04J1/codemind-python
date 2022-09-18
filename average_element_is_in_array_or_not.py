n=int(input())
a=list(map(int,input().split()))
s=s1=0
for i in a:
    s+=i
    c=s//n
for j in a:
    if c==j:
        s1+=1
        break
if s1==1:
    print("True")
else:
    print("False")
    
    
    
    