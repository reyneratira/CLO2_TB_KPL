from abc import ABC, abstractmethod
import time

# Interface for Service Strategy (Strategy Pattern Implementation)
class ServiceStrategy(ABC):
    @abstractmethod
    def simulate(self, customer, service_name, duration_minutes):
        pass

# Normal Service Strategy
class NormalService(ServiceStrategy):
    def simulate(self, customer, service_name, duration_minutes):
        print(f"\nMelayani {customer['name']} untuk {service_name} (estimasi {duration_minutes} menit)...")
        simulated_seconds = duration_minutes
        for i in range(simulated_seconds):
            print(f"  ...melayani... ({i+1}/{simulated_seconds} menit (direpresentasikan sebagai detik))")
            time.sleep(1)
        print(f"{customer['name']} telah selesai dilayani.\n")

# Fast Service Strategy
class FastService(ServiceStrategy):
    def simulate(self, customer, service_name, duration_minutes):
        print(f"\n[FAST] {customer['name']} dilayani untuk {service_name} selesai dalam 1 menit.")
        time.sleep(1)

class ServiceSimulator:
    def __init__(self, strategy: ServiceStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ServiceStrategy):
        self.strategy = strategy

    def run(self, customer, service_name, duration_minutes):
        self.strategy.simulate(customer, service_name, duration_minutes)