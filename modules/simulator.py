import time

def simulate_service(customer, services):
    code = customer['service_code']
    if code not in services:
        raise ValueError("Layanan tidak ditemukan")
    duration = services[code]['duration']
    print(f"Melayani {customer['name']} - Layanan: {services[code]['name']}")
    time.sleep(0.5)  # simulasi singkat
    print(f"Selesai dalam {duration} menit (simulasi)")