i,r,k=map(int,input().split())
s=0
for m in range(i,r+1):
    if m%k==0:
        s+=1
print(s)