"""
function called count_words that takes a string as an argument 
and returns the number of words in that string
"""

class StringLength:
    def count_words(string):
        # if input for argument is not a string is covered as well as an empty string
        if not isinstance(string, str) or string.strip() == "":
            raise Exception("Input not valid, unable to count words.")
        # split the words in string into a list of strings
        split_string = string.split()
        # len() counts the number of items in a list
        num_words = len(split_string)
        # call back the function

            
    






