def create_acronym(word):
    words = word.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym


word = input("Enter word: ")
print(create_acronym(word))  
