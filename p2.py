# s1=input("enter string 1:")
# s2=input("enter string 2:")
# s1_swapped=s2[0]+s1[1:]
# s2_swapped=s1[0]+s2[1:]
# print(s1_swapped+" "+s2_swapped)

color=[s.strip() for s in input("Enter comma sep colors:").split(',')]
print(color[::2])
