""""
function called make_snippet 
that takes a string as an argument 
and returns the first five words and 
then a '...' if there are more
"""


class FiveSnippet:
    #function called make_snippet with string arguement
    def make_snippet(string):
    #specify that arguement is string and not blank
        if not isinstance(string, str) or string.strip() == "":
            raise Exception("Input not valid, unable to count words.")
        else:
            # split the words in string into a list of strings
            split_string = string.split()
            # len() counts the number of words/items in a list
            num_words = len(split_string)
        # if number of words is equal to 5
        if num_words == 5:
            # output the original string
            return string
        # if number of words is more than 5 words
        elif num_words > 5:
            #isolate first five words
            new_string = split_string[0:5]
            # join all words in list with a space in between
            # and add an ellipsis to the end
            joined_words = " ".join(new_string) + "..."
            return joined_words
        else:
            raise Exception("String is less than five, please enter a string of 5 or more words.")    


