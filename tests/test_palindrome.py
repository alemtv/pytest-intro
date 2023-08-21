import pytest
from palindrome import is_palindrome

# Option 1
@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "bob",
    "never odd or even",
    "do geese see god",
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)

# Option 2
@pytest.mark.palindrome
@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("bob", True),
    ("never odd or even", True),
    ("do geese see god", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result