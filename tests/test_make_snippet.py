import pytest
from lib.make_snippet import FiveSnippet


# Test if string is 5 words
def test_string_five_words():
    result = FiveSnippet.make_snippet("Do not rain on my")
    assert result == "Do not rain on my"

# Test if string is more than 5 words
def test_string_is_more_than_five_words():
    result = FiveSnippet.make_snippet("Do not rain on my parade!")
    assert result == "Do not rain on my..."

# Test if string is less than 5 words
def test_string_is_less_than_five_words():
    with pytest.raises(Exception) as e:
        result = FiveSnippet.make_snippet("Don't rain")   
    error_message = str(e.value)
    assert error_message == "String is less than five, please enter a string of 5 or more words."   

# Test if string is blank
def test_if_string_is_blank():
    with pytest.raises(Exception) as e:
        result = FiveSnippet.make_snippet("")   
    error_message = str(e.value)
    assert error_message == "Input not valid, unable to count words."   

# Test if input is not a string
def test_if_string_is_blank():
    with pytest.raises(Exception) as e:
        result = FiveSnippet.make_snippet(76.89)   
    error_message = str(e.value)
    assert error_message == "Input not valid, unable to count words."   
