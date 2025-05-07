from modules.queue_manager import queue_manager
from modules.config_loader import load_services
from modules.registration import defensive_code, validation_code
from modules.simulator import simulate_service

def show_menu():
    print("\n===== SIMULASI ANTRIAN LAYANAN =====")
    print("1. Tambah Pelanggan ke Antrian")
    print("2. Tampilkan Antrian")
    print("3. Layani Pelanggan")
    print("4. Keluar")

def show_queue(qm):
    if qm.is_empty():
        print("Antrian kosong.")
    else:
        print("Antrian saat ini:")
        for idx, customer in enumerate(qm.queue, start=1):
            print(f"{idx}. {customer['name']} - {customer['service_code']}")

def main():
    services = load_services('config/services.json')
    qm = queue_manager(services)

    while True:
        show_menu()
        choice = input("Pilih menu (1-4): ")

        if choice == '1':
            try:
                name = input("Masukkan nama pelanggan: ").strip()
                
                if not name:
                    raise ValueError("Nama tidak boleh kosong")
                
                print("Daftar kode layanan yang tersedia:")
                for code, info in services.items():
                    print(f"{code}: {info['name']} ({info['duration']} menit)")

                code = input("Masukkan kode layanan (format LXX): ").strip().upper()
                validation_code(code)

                # Validasi nama + kode sekaligus (defensive_code)
                customer = defensive_code(name, code)

                # Pastikan kode layanan ada di config
                if code not in services:
                    raise ValueError("Kode layanan tidak ditemukan dalam daftar layanan")

                qm.add_to_queue(customer['services_code'], customer['name'])
                print("Pelanggan berhasil ditambahkan ke antrian.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            show_queue(qm)

        elif choice == '3':
            try:
                customer = qm.get_next_customer()
                simulate_service(customer, services)
            except IndexError as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()