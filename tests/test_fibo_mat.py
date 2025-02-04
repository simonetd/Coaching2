import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from coaching_second.mod_fibo_mat import fibonacci_matrix
import pytest


def test_fibonacci_matrix():
    # Tests de cas de base
    assert fibonacci_matrix(0) == 0
    assert fibonacci_matrix(1) == 1
    assert fibonacci_matrix(2) == 1
    assert fibonacci_matrix(3) == 2
    assert fibonacci_matrix(4) == 3
    assert fibonacci_matrix(5) == 5
    assert fibonacci_matrix(6) == 8
    assert fibonacci_matrix(10) == 55
    assert fibonacci_matrix(20) == 6765
    
    # Test d'un grand nombre
    assert fibonacci_matrix(50) == 12586269025
    
    # Test d'entrée invalide
    with pytest.raises(ValueError):
        fibonacci_matrix(-1)
    
    with pytest.raises(TypeError):
        fibonacci_matrix("string")
        fibonacci_matrix(5.5)
