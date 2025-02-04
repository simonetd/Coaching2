import statistics
from abc import ABC, abstractmethod

class StatisticsStrategy(ABC):
    @abstractmethod
    def calculate(self, prices):
        pass

class MeanAndStdStrategy(StatisticsStrategy):
    def calculate(self, prices):
        bid_prices, ask_prices = zip(*prices) if prices else ([], [])
        bid_mean = statistics.mean(bid_prices) if bid_prices else 0
        ask_mean = statistics.mean(ask_prices) if ask_prices else 0
        bid_std = statistics.stdev(bid_prices) if len(bid_prices) > 1 else 0
        ask_std = statistics.stdev(ask_prices) if len(ask_prices) > 1 else 0
        return bid_mean, ask_mean, bid_std, ask_std
