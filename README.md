# pytest Intro
___
To install the latest version of pytest, execute the following command
```
pip install pytest
```

Run the test using the following command
```
python -m pytest 
```

To execute the tests from a specific file, use the following syntax
```
pytest <filename> -v
```
___
## Markers
Markers are applied on the tests using the syntax given below
```
@pytest.mark.<markername>
```

To run the marked tests, we can use the following syntax −
```
pytest -m <marker>
```

pytest provides a few marks out of the box:
```
skip - skips a test unconditionally.
skipif - skips a test if the expression passed to it evaluates to True.
xfail - indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.
parametrize - creates multiple variants of a test with different values as arguments. Please check test_palindrome.py.
```