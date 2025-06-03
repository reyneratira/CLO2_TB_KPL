from typing import Optional, Dict, List
from modules.utils import print_error
from modules.queue_manager import QueueManager
from modules.config_loader import load_services
from modules.registration import create_valid_customer_data, services_code_validation
from modules.simulator import ServiceSimulator, NormalService, FastService

class AppFacade:
    def show_menu() -> None:
        print("\n===== SIMULASI ANTRIAN LAYANAN =====")
        print("1. Tambah Pelanggan ke Antrian")
        print("2. Tampilkan Antrian")
        print("3. Layani Pelanggan")
        print("4. Ganti Mode Simulasi")
        print("5. Keluar")
        print("=====================================")
    
    # Application Facade for Service Queue Simulation
    def __init__(self, config_path: str = 'config/services.json', queue: Optional[QueueManager] = None, sim: Optional[ServiceSimulator] = None) -> None:
        self.services: Dict[str, Dict[str, str]] = load_services(config_path)
        self.qm: QueueManager = QueueManager(self.services)
        self.simulator: ServiceSimulator = ServiceSimulator(NormalService())

    # List available services
    def list_services(self) -> Dict[str, Dict[str, str]]:
        return self.services
    
    def handle_add_customer(self) -> None:
        name: str = input("Masukkan nama pelanggan: ").strip()
        if not name:
            raise ValueError("Nama tidak boleh kosong")

        print("Kode layanan tersedia:")
        for code, data in self.list_services().items():
            print(f"{code}: {data['name']} (Estimasi waktu: {data['duration']} menit)")
        
        services_code: str = input("Masukkan kode layanan (misal: L01): ").strip().upper()
    
        try:
            # Validate data input using the registration module
            customer: Optional[Dict[str, str]] = create_valid_customer_data(name, services_code)
            if customer:
                # Setelah lolos validasi, input diproses
                self.add_customer(customer['services_code'], customer['name'])
                print("Pelanggan berhasil ditambahkan ke antrian.\n")
            else:
                raise ValueError("Data pelanggan tidak valid")
        except ValueError as e:
            print_error(e)

    # Add a customer to the queue
    def add_customer(self, service_code: str, name: str) -> None:
        self.qm.add_to_queue(service_code, name)

    # Get the current queue of customers
    def get_queue(self) -> List[Dict[str, str]]:
        return list(self.qm.queue)

    # Serve the next customer in the queue
    def serve_next_customer(self) -> None:
        if self.qm.is_empty():
            raise IndexError("Antrian kosong")
        customer: Dict[str, str] = self.qm.get_next_customer()
        service_name: str = self.qm.get_service_name(customer['service_code'])
        duration: int = self.qm.get_service_time(customer['service_code'])
        self.simulator.simulate_service(customer, service_name, duration)

    # Set the simulation mode (normal or fast)
    def set_simulation_mode(self, mode: str = 'normal') -> None:
        if mode == 'normal':
            self.simulator.set_strategy(NormalService())
        elif mode == 'fast':
            self.simulator.set_strategy(FastService())
        else:
            raise ValueError("Mode tidak dikenal")