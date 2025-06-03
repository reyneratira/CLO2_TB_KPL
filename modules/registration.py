import re
from typing import Dict

def services_code_validation(code: str) -> bool:
    pattern: str = r'^L[0-9]{2}$'
    return bool(re.match(pattern, code))

def create_valid_customer_data(name: str, services_code: str) -> Dict[str, str]:
    if not name:
        raise ValueError("Nama tidak boleh kosong")
    if not services_code_validation(services_code):
        raise ValueError("Kode harus sesuai format LXX")
    
    return {
        'name': name,
        'services_code': services_code
    }