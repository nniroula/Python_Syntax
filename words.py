
#1.  For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to 
# uppercase? Ask Python for help on what you can do with strings! 
words = ["apple", "orange", "mango"]
for word in words:
    print(word.upper())

# To change to uppercase, use a method called upper().

# 2. Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(words):
    """ This function converts all letters in words into upper case letters  """
    for word in words:
        print(word.upper())
print_upper_words(["apple", "orange", "mango"])

#3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
def print_e_words(words):
    """ This function prints all words that start with letter e or E """
    for word in words:
        if word[0].lower() == 'e':
            print(word)      
print_e_words(["apple", "orange", "mango", "Egg", "edge"])

#4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that 
# start with one of those letters.

def print_different_words(words, must_start_with):
    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word)
                
print_different_words(["good", "Nabin", "better"], must_start_with = {"N", "b"})

