n=int(input('n:'))
for i in range(n):
    for j in range(n):
        if(j==0 or (i==0 and j<=n//2) or (i==n//2 and j<=n//2) or (j==n//2 and i<=n//2) or (i-j==n//2)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()