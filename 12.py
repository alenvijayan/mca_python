n=int(input('enter number:'))
factor=[]
for i in range(1,n+1):
    if not n%i:
        factor.append(i)
print("factos:",factor)