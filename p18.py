word=input('enter word:')
if word.endswith('ing'):
    print(word+'ly')
    word=word.replace('ing','mbg')
    print(word)
else:
    print(word+'ing')