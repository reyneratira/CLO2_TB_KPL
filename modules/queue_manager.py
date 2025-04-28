from collections import deque

class queue_manager:
    def __init__(self, services_data):
        self.queue = deque()
        self.service_time_mapping = services_data
    
    def add_to_queue(self, service_code, customer_name):
        if not customer_name:
            raise ValueError("Nama pelanggan tidak boleh kosong")
        if service_code not in self.service_time_mapping:
            raise ValueError("Kode layanan tidak valid")
        
        self.queue.append({
            'name': customer_name,
            'service_code': service_code
        })
    
    def get_next_customer(self):
        if not self.queue:
            raise IndexError("Antrian kosong")
        return self.queue.popleft()
    
    def is_empty(self):
        return len(self.queue) == 0

    def peek_next_customer(self):
        if not self.queue:
            raise IndexError("Antrian kosong")
        return self.queue[0]

    def get_service_time(self, service_code):
        if service_code not in self.service_time_mapping:
            raise ValueError("Kode layanan tidak valid")
        return self.service_time_mapping[service_code]['duration']
    
    def get_service_name(self, service_code):
        if service_code not in self.service_time_mapping:
            raise ValueError("Kode layanan tidak valid")
        return self.service_time_mapping[service_code]['name']