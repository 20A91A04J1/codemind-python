n=int(input())
s=0
s1=1
t=n
while n>0:
    d=n%10
    s+=d
    s1*=d
    n=n//10
if s==s1:
    print('Spy Number')
else:
    print('Not Spy Number')