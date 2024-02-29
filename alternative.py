original_string = "I hope you all had a Merry Christmas and a Happy New Year!"
# setting original string variable

# Initialize result string 
alternate_string = "" 
 
# Loop over characters in the string 
for i, char in enumerate(original_string): 
    # Convert character to upper or lower case 
    if i % 2 == 0: 
        alternate_string += char.upper() 
    # converting characters devisable bt 2 to uppercase 
    else: 
        alternate_string += char.lower() 
    #  all other characters to lowercase 

print(alternate_string)         
# Print alternate_string


# splitting original string under new variable
alternate_word = original_string.split()   


# Empty string to store a to be split list of words, 
words_sep = ""

# block code to make every alternate word
for i in range(0, len(alternate_word)): #loop to make every second letter upper
    # Make all even words lowercase
    if i % 2 == 0:
        words_sep = words_sep + " "+ alternate_word[i].lower() 
    # Make all other words uppercase 
    else:
        words_sep = words_sep + " " + alternate_word[i].upper() 
    

# Block code to join the individual characters
upper_lower = "".join(words_sep)

# Block code to product the final results
print(upper_lower)
