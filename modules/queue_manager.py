from collections import deque
from typing import Dict, Deque

class QueueManager:
    def __init__(self, services_mapping:  Dict[str, Dict[str, str]]) -> None:
        self.queue: Deque[Dict[str, str]] = deque()
        self.service_time_mapping = services_mapping
    
    def add_to_queue(self, service_code: str, customer_name: str) -> None:
        if not customer_name:
            raise ValueError("Nama pelanggan tidak boleh kosong")
        if service_code not in self.service_time_mapping:
            raise ValueError("Kode layanan tidak valid")
        
        self.queue.append({
            'name': customer_name,
            'service_code': service_code
        })
    
    def get_next_customer(self) -> Dict[str, str]:
        if not self.queue:
            raise IndexError("Antrian kosong")
        return self.queue.popleft()
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def peek_next_customer(self) -> Dict[str, str]:
        if not self.queue:
            raise IndexError("Antrian kosong")
        return self.queue[0]

    def get_service_time(self, service_code: str) -> int:
        if service_code not in self.service_time_mapping:
            raise ValueError("Kode layanan tidak valid")
        return self.service_time_mapping[service_code]['duration']
    
    def get_service_name(self, service_code: str) -> str:
        if service_code not in self.service_time_mapping:
            raise ValueError("Kode layanan tidak valid")
        return self.service_time_mapping[service_code]['name']