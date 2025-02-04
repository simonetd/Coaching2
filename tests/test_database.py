import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from coaching_second.database import DatabaseManager
import pytest

def test_database_insert():
    db = DatabaseManager(":memory:")  # Utilisation d'une base en mémoire pour le test
    db.insert_data(1, 20.5, 21.0, 5000, 6000)
    
    result = db.fetch_last_n_prices(1)
    assert len(result) == 1
    assert 20 <= result[0][0] <= 50
    assert 20 <= result[0][1] <= 50
