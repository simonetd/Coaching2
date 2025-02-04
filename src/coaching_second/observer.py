from abc import ABC, abstractmethod
import time

class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class PriceDataObserver(Observer):
    def __init__(self):
        self.buffer = {}  # Stockage temporaire des données
        self.last_flush_time = time.time()

    def update(self, data):
        """Stocke les données temporairement en mémoire."""
        for instrument_id, (bid, ask, bid_qty, ask_qty) in data.items():
            if instrument_id not in self.buffer:
                self.buffer[instrument_id] = []
            self.buffer[instrument_id].append((bid, ask))

        # On ne stocke plus rien en base ici !

    def flush(self):
        """Renvoie les données stockées en mémoire puis vide le buffer."""
        temp_data = self.buffer.copy()
        self.buffer.clear()
        return temp_data
