from modules.app_facade import AppFacade
from modules.utils import print_error

def main() -> None:
    # Initialize the application facade
    app: AppFacade = AppFacade()

    while True:
        AppFacade.show_menu()
        choice: str = input("Pilih menu (1-5): ").strip()

        if choice == '1':
            try:
                app.handle_add_customer()
            except ValueError as e:
                print_error(e)
            
        elif choice == '2':
            queue: list[dict[str, str]] = app.get_queue()
            if not queue:
                print("Antrian kosong.")
            else:
                for i, customer in enumerate(queue, 1):
                    print(f"{i}. {customer['name']} - Kode Layanan: {customer['service_code']}")

        elif choice == '3':
            try:
                app.serve_next_customer()
                print("Pelanggan telah dilayani.")
            except IndexError as e:
                print_error(e)

        elif choice == '4':
            print("Pilih mode simulasi:")
            print("1. Normal")
            print("2. Fast")
            mode: str = input("Masukkan pilihan (1-2): ").strip()
            try:
                if mode == '1':
                    app.set_simulation_mode('normal')
                    print("Mode simulasi diatur ke Normal.")
                elif mode == '2':
                    app.set_simulation_mode('fast')
                    print("Mode simulasi diatur ke Fast.")
                else:
                    raise ValueError("Pilihan tidak valid. Harap masukkan 1 atau 2.")
            except ValueError as e:
                print_error(e)

        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi simulasi antrian layanan.")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1-5.")

# Main entry point for the application
if __name__ == "__main__":
    main()