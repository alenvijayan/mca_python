# words=input('enter comma sepp words:').split(',')
# words.sort(key=len)
# print("longest word:",words[-1])

#or

words=[s.strip() for s in input('enter comma sepp words:').split(',')]
sorted_words=sorted(words,key=len) #sorted gives a list as op
print("longest word:",sorted_words[-1])
