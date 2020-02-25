# -*- coding: utf-8 -*-
"""
Muhammad Mashwani
Homework #4
PeopleSoft ID: 1378052
"""

# Get the signature of a word
def get_sig(word):
    temp = list(word)
    temp.sort()
    return "".join(temp)

# Find all the anagrams in a list of words
def get_anagrams(word_list):
    result = {}
    for word in word_list:
        sig = get_sig(word)
        if sig not in result:
            result[sig] = []
        result[sig].append(word)
    return result
choice = 1
while choice != 0:
    words_dict = {} # The dictionary of words
    words = [] # All the words in the file
    with open("words_4.txt") as file:
        for word in file.readlines():
            word = word.strip()
            if len(word) not in words_dict:
                words_dict[len(word)] = []
            words_dict[len(word)].append(word)
            
    final = {} # The final result dictionary
    for i in range(2,15):
        temp = get_anagrams(words_dict[i])
        for item in temp:
            a_list = temp[item]
            list_length = len(a_list)
            if list_length not in final:
                final[list_length] = []
            final[list_length].append(a_list)

    the_keys = final.keys() # The anagram list lengths
    msg = "Please enter the anagram group size({}-{} or 0 to quit): ".format(min(the_keys), max(the_keys))
    choice = int(input(msg))
    if choice in final:
        for item in final[choice]:
            print(item)
    elif choice == 0:
        print("Thank you!")
    else:
        print("That option is not available!")
