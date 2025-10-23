# n=int(input("Enter limit:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(" * ",end='')
#     print()

n = int(input("Enter limit: "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)


