import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from coaching_second.price_generator import RandomPriceGenerator

def test_generate_price():
    generator = RandomPriceGenerator()
    instrument_id = 0
    bid, ask, bid_qty, ask_qty = generator.generate_price(instrument_id)
    
    assert 10 <= bid <= 50
    assert bid < ask
    assert 1000 <= bid_qty <= 10000
    assert 1000 <= ask_qty <= 10000
