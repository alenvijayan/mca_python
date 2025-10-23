# word=input('enter word:')
# freq={}
# for i in word:
#     freq[i]=freq.get(i,0)+1
# print('frequency:',freq)

# names=[s.strip() for s in input('enter , sepp names:').split(',')]
# count=sum(1 for s in names if s.lower().startswith('a'))
# print('number of names starting with a:',count)


text=input("Enter a text:").split()
for i in text:
    print(i)