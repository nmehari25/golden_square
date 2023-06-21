from lib.counter import *

# def test_reminds_the_user_to_do_a_task():
#     reminder = Reminder("Kay")
#     reminder.remind_me_to("Walk the dog")
#     result = reminder.remind()
#     assert result == "Walk the dog, Kay!"

# Counts no people
def test_none_are_counted():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."



# Add just 1 number
def test_counter_adds_one_num():
    counter = Counter()
    counter.add(1)
    assert counter.report() == "Counted to 1 so far."

# Add many numbers
def test_add_many_numbers():
    counter = Counter()
    counter.add(6)
    counter.add(2)
    assert counter.report () == "Counted to 8 so far."

# Enter negative numbers 

def test_add_negative_number():
    counter = Counter()
    counter.add(-1)
    assert counter.report() == "Counted to -1 so far."

# Enter number which is a float

def test_add_float_number():
    counter = Counter()
    counter.add(4.567)
    assert counter.report() == "Counted to 4.567 so far."
