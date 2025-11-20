# Display alternate characters from a line of text using recursion.

def alternate_chars(s, index=0):
    if index >= len(s):
        return ""
    return s[index] + alternate_chars(s, index + 2)

line = input("Enter a line of text: ")
result = alternate_chars(line)
print("Alternate characters:", result)
