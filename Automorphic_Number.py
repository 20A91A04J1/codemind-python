n=int(input())
a=str(n)
b=n**2
c=b%10**len(a)
if c==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    