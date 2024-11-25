# tests/test_main.py

from src.main import add

def test_add():
    # Basic integer addition
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
    # Large numbers
    assert add(999999, 1) == 1000000
    
    # Negative numbers
    assert add(-5, -7) == -12
    assert add(-10, 5) == -5
    
    # Floating point numbers
    assert add(2.5, 3.7) == 6.2
    assert add(-1.5, 2.5) == 1.0