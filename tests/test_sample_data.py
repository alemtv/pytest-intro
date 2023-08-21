import pytest
import time

@pytest.mark.sample_data
def test_sample_data():
    pass

def test_slow_tc():
    time.sleep(2)
    pass