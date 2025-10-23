# n=int(input("enter n:"))    ##O
# for i in range(n):
#     for j in range(n):#here j range is also n to make a grid
#         if(i==n-1 or  i==0 or j==0 or j==n-1 ):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
        
#     print()


# n=int(input("enter n(odd number):")) ##M
# for i in range(n):
#     for j in range(n):#here j range is also n to make a grid
#         if(j==0 or j==n-1 or(i==j and i<=n//2) or (j==n-1-i and i<=n//2)):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
        
#     print()

# n=int(input("enter n:"))     ##K
# for i in range(n):
#     for j in range(n):#here j range is also n to make a grid
#         if(j==0 or (i+j==n//2) or (i-j==n//2)):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
        
#     print()


# n=int(input("Enter n:"))     #L
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1 or(i==j)):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n=int((input("Enter n:")))    #Z
# for i in range(n):
#     for j in range(n):
#         if(i==0 or i==n-1 or(j==n-1-i)):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n=int(input('Enter n:'))            #V
# for i in range(n):
#     for j in range(2*n):
#         if(i==j or j==2*n-1-i-1):  
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# n=int(input('Enter n:'))            #V(without row * 2)
# for i in range(n):
#     for j in range(n):
#         if((i==j and i<=n//2) or (j==n-1-i and i<n//2)):  
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n=int(input('Enter n:'))        #R
# for i in range(n):
#     for j in range(n):
#         if(((i==0 and j<=n//2) and i<=n//2)or j==0 or (i==n//2 and j<=n//2) or (j==n//2 and i<=n//2) or (i-j==n//2)):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()