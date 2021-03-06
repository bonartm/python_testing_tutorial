"""
Examples of border cases

TASK: fill in the gaps, so that all tests pass
"""

import pytest
from mobydick.word_counter import count_words



def test_empty():
    """Empty input works"""
    text = ''
    assert count_words(text) == _____

def test_smallest():
    """Minimal string works."""
    text = "whale"
    assert ____ == ____

def test_typical():
    """Representative input works."""
    text = "whale eats captain"
    assert ____

def test_wrong_input():
    """Non-string fails with a specific error"""
    with pytest.raises(_____) as e_info:
        count_words(777)

def test_biggest():
    """An entire book works."""
    text = open('mobydick_full.txt').read()
    assert _____ > 200000

def test_nasty1():
    text = """you haint no objections to sharing a harpooneer's blanket,
have ye? I s'pose you are goin' a-whalin',
so you'd better get used to that sort of thing."""
    assert count_words(text) == _____

def test_nasty2():
    """Another ugly data example works."""
    text = """That #~&%* program still doesn't work!
I already de-bugged it 3 times, and still numpy.array keeps throwing AttributeErrors.
What should I do?"""
    _____
