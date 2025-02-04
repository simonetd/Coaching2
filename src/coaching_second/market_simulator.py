import time
import threading
import random
from database import DatabaseManager
from price_generator import RandomPriceGenerator, INSTRUMENT_IDS
from observer import PriceDataObserver
from strategy import MeanAndStdStrategy

UPDATE_INTERVAL = 1
CALC_INTERVAL = 10
NUM_SAMPLES = 10

class MarketSimulator:
    def __init__(self):
        self.database = DatabaseManager()
        self.generator = RandomPriceGenerator()
        self.observer = PriceDataObserver()
        self.strategy = MeanAndStdStrategy()
    
    def run(self):
        while True:
            # Génération de 100 nouvelles données par instrument stockées en mémoire
            for _ in range(100):  
                data = {inst: self.generator.generate_price(inst) for inst in INSTRUMENT_IDS}
                self.observer.update(data)  # Stockage temporaire en mémoire
            
            # Calcul des statistiques toutes les 10 secondes
            if time.time() % CALC_INTERVAL < UPDATE_INTERVAL:
                data_buffer = self.observer.flush()  # Récupération des données en mémoire

                print("\n **Statistiques par instrument ID** ")
                for inst in INSTRUMENT_IDS:
                    if inst in data_buffer and len(data_buffer[inst]) >= NUM_SAMPLES:
                        sample = random.sample(data_buffer[inst], NUM_SAMPLES)  # Sélection aléatoire de 10 valeurs
                    else:
                        sample = data_buffer.get(inst, [])  # Si on a moins de 10 valeurs, on prend tout

                    if sample:
                        bid_mean, ask_mean, bid_std, ask_std = self.strategy.calculate(sample)
                    
                        # Affichage des résultats
                        print(f" {inst} -> Bid Mean: {bid_mean:.2f}, Ask Mean: {ask_mean:.2f}, Bid Std: {bid_std:.2f}, Ask Std: {ask_std:.2f}")
                    
                        # Insérer les statistiques en base
                        self.database.insert_statistics(inst, bid_mean, ask_mean, bid_std, ask_std)

            time.sleep(UPDATE_INTERVAL)


if __name__ == "__main__":
    simulator = MarketSimulator()
    thread = threading.Thread(target=simulator.run)
    thread.start()
