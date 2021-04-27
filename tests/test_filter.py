from utils import listener

def test_filter_positive():
    assert listener.check_for_profanity("Fuck this semester")

def test_filter_negative():
    assert not listener.check_for_profanity("I hate this semester")
