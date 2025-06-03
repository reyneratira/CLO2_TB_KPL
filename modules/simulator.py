from abc import ABC, abstractmethod
import time
from typing import Dict

# Interface for Service Strategy (Strategy Pattern Implementation)
class ServiceStrategy(ABC):
    @abstractmethod
    def simulate(self, customer: Dict[str, str], service_name: str, duration_minutes: int) -> None:
        pass

# Normal Service Strategy
class NormalService(ServiceStrategy):
    def simulate(self, customer: Dict[str, str], service_name: str, duration_minutes: int) -> None:
        print(f"\nMelayani {customer['name']} untuk {service_name} (estimasi {duration_minutes} menit)...")
        simulated_seconds: int = duration_minutes
        for i in range(simulated_seconds):
            print(f"  ...melayani... ({i+1}/{simulated_seconds} menit (direpresentasikan sebagai detik))")
            time.sleep(1)
        print(f"{customer['name']} telah selesai dilayani.\n")

# Fast Service Strategy
class FastService(ServiceStrategy):
    def simulate(self, customer: Dict[str, str], service_name: str, duration_minutes: int) -> None:
        print(f"\n[FAST] {customer['name']} dilayani untuk {service_name} selesai dalam 1 menit. (dari {duration_minutes} menit yang sebenarnya)")
        time.sleep(1)

class ServiceSimulator:
    def __init__(self, strategy: ServiceStrategy) -> None:
        self.strategy: ServiceStrategy = strategy

    def set_strategy(self, strategy: ServiceStrategy) -> None:
        self.strategy: ServiceStrategy = strategy

    def simulate_service(self, customer: Dict[str, str], service_name: str, duration_minutes: int) -> None:
        self.strategy.simulate(customer, service_name, duration_minutes)