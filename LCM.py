a,b=map(int,input().split())
if a>b:
    mad=a
else:
    mad=b
while True:
    if mad%a==0 and mad%b==0:
        print(mad)
        break
    mad+=1