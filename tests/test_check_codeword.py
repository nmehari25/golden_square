
from lib.check_codeword import *

"""
If given an empty string
It returns an empty string
"""
def test_given_empty_string_returns_empty_string():
    result = ("")
    assert result == ""

"""
If given the string 'horse'
It returns the string 'Correct! Come in.'
"""
def test_string_is_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

"""
If string has the correct first and last letter
returns 'Close, but nope.'
"""
def correct_first_and_last_letter():
    result = check_codeword("hope")
    assert result == "Close, but nope."

"""
If the codeword is wrong
returns 'Wrong!'
"""
def codeword_is_wrong():
    result = check_codeword("xysrp")
    assert result == "Wrong!"
    
    