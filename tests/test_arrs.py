from utils import arrs
import pytest

@pytest.fixture
def array_fixture():
    return [1, 2, 3]

@pytest.fixture
def array_fixture_long():
    return [1, 2, 3, 4]

def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(array_fixture, -1, "test") == "test"


def test_slice(array_fixture, array_fixture_long):
    assert arrs.my_slice(array_fixture_long, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(array_fixture_long, -5, 3) == [1, 2, 3]
    assert arrs.my_slice(array_fixture_long, -2, 3) == [3]