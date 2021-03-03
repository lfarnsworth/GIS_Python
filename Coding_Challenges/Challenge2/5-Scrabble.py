# Given Dictionary
letter_scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}

# Ask user to enter word
word_str = input("Enter a word: ")

# Start score at zero (initialize the variable)
calculated_score = 0

# Step through word string letter by letter
for letter in word_str:
    # get list of keys, search for letter later
    list_of_keys = letter_scores.keys()
    # step through each item in the list
    for key_item in list_of_keys:
        # check if the letter is in the current item
        if letter in key_item:
            # Find number associated with the key
            this_letters_score = letter_scores.get(key_item)
            # Add score to the running tally
            calculated_score = calculated_score + this_letters_score
print("Your score is: " + str(calculated_score))

# Feedback - The way you coded this succesfully avoided my intended failures - i.e. if I add in a space to my input
# most times it causes a keyerror (not in dictionary basically). You save this by the for loop/if in, exceptional.
