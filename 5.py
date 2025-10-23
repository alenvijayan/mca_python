# dict={1:2,2:3,3:4,4:56}
# print(dict)
# k=int(input('Enter key'))
# print('exist' if k in dict.keys() else "not")

# dic1={1:2,2:4,3:9,4:16}
# dic2={2:16,4:20,5:200,'alice':'hi','age':25}
# print(dic1)
# print(dic2)
# dic1.update(dic2)
# print(dic1)

# dic1={1:2,2:4,3:55,4:16,9:66,8:4,5:2}
# print(dic1)
# print('Ascending:',sorted(dic1.items(),reverse=True))

dic1={1:2,2:4,3:55,4:16,9:66,8:4,5:2}
print(dic1)
inv_dict={y:x for x,y in dic1.items()}
print(inv_dict)