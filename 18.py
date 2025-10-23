txt=input('enter text:').split()
longest_word=max(len(x) for x in txt)
print('longest word lengt:',longest_word)
res=[x for x in txt if len(x)==longest_word]
print(res)
if(len(res)>1):
    print('BINGO')
