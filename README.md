# Grouping-together-anagrams-from-a-list-of-words
Write a program that makes use of strings, lists, dictionaries, and files as well as functions, conditional execution, and looping to extract and and display information from a file. 


# Problem:  
- Write a program that will read the words contained in a file and group together into lists, the words that are anagrams for each other. - Allow the user to request all the words for a group of a certain size.
- Read the all the words from the file “words.txt”.
- Group together into lists, the words that are anagrams for each other.
- Accept input from the user on size of group to display, i.e. the number of words that are anagrams for each other, validating that this size falls within a reasonable range.
- Display all groups of words of the specified size, with each group printed together.
- Allow the user to enter additional requests or to exit.
- Use good functional style and suitable variable names.  
# Expected Output:  
- Given a data file that contains: EAT, ATE, TEA, CAT, ACT, EYE, SEE 
- Please enter the anagram group size (1-3) or 0 to quit: 1

                [EYE] [SEE]
- Please enter the anagram group size (1-3) or 0 to quit: 3

              [ATE, EAT, TEA]
- Please enter the anagram group size (1-3) or 0 to quit: 0

                 Thank you! 
