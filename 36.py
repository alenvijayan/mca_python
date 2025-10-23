def sum_wh(n):
    if n==0:
        return 0
    else:
        return n+sum_wh(n-1)

n=int(input('lim:'))
print('sum:',sum_wh(n))