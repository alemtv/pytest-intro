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