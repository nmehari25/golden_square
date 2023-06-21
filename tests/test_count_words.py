import pytest
from lib.count_words import StringLength


# Test if string is empty
def test_an_empty_string():
    with pytest.raises(Exception) as e:
        StringLength.count_words("") 
    error_message = str(e.value)
    assert error_message == "Input not valid, unable to count words."

# Test if string is not a string
def test_is_type_string():
    with pytest.raises(Exception) as e:
        StringLength.count_words(56665) 
    error_message = str(e.value)
    assert error_message == "Input not valid, unable to count words."


