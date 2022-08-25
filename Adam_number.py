n=int(input())
a=n*n
n=str(n)
b=int(n[::-1])
c=str(b*b)
if int(c[::-1])==a:
    print("True")
else:
    print("False")