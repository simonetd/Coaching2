import random
import string
from abc import ABC, abstractmethod

PRICE_MIN, PRICE_MAX = 10, 50
QUANTITY_MIN, QUANTITY_MAX = 1000, 10000
NUM_INSTRUMENTS = 10  # Seulement 10 instruments

def generate_instrument_ids():
    """Génère une liste de 10 identifiants uniques de 4 lettres."""
    return [''.join(random.choices(string.ascii_uppercase, k=4)) for _ in range(NUM_INSTRUMENTS)]

INSTRUMENT_IDS = generate_instrument_ids()  # Liste des IDs d'instruments

class PriceGenerator(ABC):
    @abstractmethod
    def generate_price(self, instrument_id):
        pass

class RandomPriceGenerator(PriceGenerator):
    def __init__(self):
        self.instrument_prices = {inst: random.uniform(PRICE_MIN, PRICE_MAX) for inst in INSTRUMENT_IDS}
    
    def generate_price(self, instrument_id):
        last_price = self.instrument_prices[instrument_id]
        change = random.uniform(-0.1, 0.1)  # Volatilité modérée
        new_bid_price = max(PRICE_MIN, min(PRICE_MAX, last_price + change))
        new_ask_price = new_bid_price + random.uniform(0.1, 1.0)
        bid_quantity = random.randint(QUANTITY_MIN, QUANTITY_MAX)
        ask_quantity = random.randint(QUANTITY_MIN, QUANTITY_MAX)
        self.instrument_prices[instrument_id] = new_bid_price
        return new_bid_price, new_ask_price, bid_quantity, ask_quantity
