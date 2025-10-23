# dic1={1:2,2:4,3:9,4:16}
# print(dic1)
# k=int(input('enter key:'))
# print('exist:',k in dic1.keys())

# dic1={1:2,2:4,3:9,4:16}
# dic2={2:16,4:20,5:200,'alice':'hi','age':25}
# print(dic1)
# print(dic2)
# dic1.update(dic2)
# print(dic1)

dic1={1:2,2:4,3:55,4:16,9:66,8:4,5:2}
print(dic1)
print('Ascending:',dict(sorted(dic1.items())))
print('descending:',sorted(dic1.items(),reverse=True))

# dic1={1:2,2:4,3:55,4:16,9:66,8:4,5:2}
# print(dic1)
# inverted_dic1={v:k for k,v in dic1.items()}  #wWhen two keys have the same value, the last key encountered overwrites the previous one in the inverted dictionary.t 
# print(inverted_dic1)
