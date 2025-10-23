text=input('enter text:').split()


length_words=[len(x) for x in text]
longest_word=max(length_words)

words=[x for x in text if len(x)==longest_word]
print(words)
print(longest_word)

if len(words)>1:
    print("BINGO")
    

# text = input('Enter text: ')
# words = text.split()  # splits text into a list of words

# lengths = [len(w) for w in words]  # list of word lengths
# max_len = max(lengths)  # find longest word length

# # find all words that match this max length
# longest_words = [w for w in words if len(w) == max_len]

# print("Length of longest word:", max_len)

# # if more than one word shares the same max length
# if len(longest_words) > 1:
#     print("BINGO")
# else:
#     print("Longest word:", longest_words[0])
