from utils import listener

## @story{8}
def test_filter_positive():
    assert listener.check_for_profanity("Fuck this semester")

## @story{8}
def test_filter_negative():
    assert not listener.check_for_profanity("I hate this semester")
