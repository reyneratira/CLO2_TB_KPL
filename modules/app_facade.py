from modules.queue_manager import queue_manager
from modules.config_loader import load_services
from modules.registration import defensive_code, validation_code
from modules.simulator import ServiceSimulator, NormalService, FastService

class AppFacade:
    def show_menu():
        print("\n===== SIMULASI ANTRIAN LAYANAN =====")
        print("1. Tambah Pelanggan ke Antrian")
        print("2. Tampilkan Antrian")
        print("3. Layani Pelanggan")
        print("4. Ganti Mode Simulasi")
        print("5. Keluar")
        print("=====================================")
    
    # Application Facade for Service Queue Simulation
    def __init__(self, config_path='config/services.json'):
        self.services = load_services(config_path)
        self.qm = queue_manager(self.services)
        self.simulator = ServiceSimulator(NormalService())

    # List available services
    def list_services(self):
        return self.services

    # Add a customer to the queue with validation
    def add_customer(self, name, code):
        if not validation_code(code):
            raise ValueError("Kode layanan harus dalam format LXX")
        customer = defensive_code(name, code)
        if code not in self.services:
            raise ValueError("Kode layanan tidak tersedia")
        self.qm.add_to_queue(code, name)

    # Get the current queue of customers
    def get_queue(self):
        return list(self.qm.queue)

    # Serve the next customer in the queue
    def serve_next_customer(self):
        if self.qm.is_empty():
            raise IndexError("Antrian kosong")
        customer = self.qm.get_next_customer()
        service_name = self.qm.get_service_name(customer['service_code'])
        duration = self.qm.get_service_time(customer['service_code'])
        self.simulator.run(customer, service_name, duration)

    # Set the simulation mode (normal or fast)
    def set_simulation_mode(self, mode='normal'):
        if mode == 'normal':
            self.simulator.set_strategy(NormalService())
        elif mode == 'fast':
            self.simulator.set_strategy(FastService())
        else:
            raise ValueError("Mode tidak dikenal")