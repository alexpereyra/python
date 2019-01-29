# Start with an empty dictionary
words = {}
# Get a word from the user
value = input("Please enter a word (or -999 to quit): ")

# As long as the user didn't enter -999, let's work with the dictionary
while (value != '-999'):
    if value in words:
        # The word has already been entered, increment the number of time
        #  entered by 1
        words[value] = words[value] + 1
    else:
        # this is a brand new word, so let's put it in the dictionary
        #  and start the number of times entered at 1
        words[value] = 1

    # Get another value from the user
    value = input("Please enter a word (or -999 to quit): ")

# The user is done entering words, let's generate some output
print ("dictionary order")

# Print out a listing of all the words and the number of times entered
for current_key in words.keys():
    print (current_key, '\t', words[current_key])

# Now let's display the list, but sorted by the word
print ("\nsorted keys")
my_keys = list(words.keys())
my_keys.sort()

for current_key in my_keys:
    print (current_key, '\t', words[current_key] )

# Finally, let's display the list sorted by number of times entered
print ("\nsorted values")

# Sorting based on values
temp_list = []

# Select a key in the dictionary
for current_key in words.keys():
    # determine the number of words in the sorted list
    list_length = len(temp_list)

    # start looking at position 0
    placeholder = 0

    # As long as there are still items in the list
    while placeholder < list_length:
        # Get the word in the sorted list
        list_key = temp_list[placeholder]

        # Determine if this word has been entered
        #   more times than the current word
        if words[list_key] > words[current_key]:
            break

        # It wasn't, so let's look at the next word
        #   in the sorted list
        placeholder = placeholder + 1

    # We found the location in the sorted list for
    #   this word, insert it
    temp_list.insert(placeholder, current_key)

# Everything is sorted, go ahead and print out the results
for current_key in temp_list:
    print (current_key, '\t', words[current_key])
