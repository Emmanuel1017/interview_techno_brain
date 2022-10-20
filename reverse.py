
def reverse_string():
 string = input("enter your words")
 words = string.split()
 words = list(reversed(words))
 new_words =  [item.replace("  ", " ") for item in words]
 print(" ".join(new_words))
reverse_string()
