# CLO2_TB_KPL – Simulasi Sistem Antrian Layanan

## Deskripsi
Aplikasi CLI berbasis Python untuk menyimulasikan antrian layanan seperti bank atau layanan publik. Setiap pelanggan akan mendaftar, masuk ke antrian, dan dilayani sesuai jenis layanan yang dipilih.

## Kelompok 3
- Ilham Lii Assidaq – Modul Registrasi & Validasi
- Aulia Jasifa BR Ginting – Modul Manajemen Antrian
- Alvin Bagus F – Modul Simulasi Proses Layanan
- Reyner Atira Prasetyo – Modul Load Konfigurasi & Testing

## Fitur
- Validasi pelanggan menggunakan automata (regex)
- Antrian layanan dengan FIFO menggunakan library built-in
- Simulasi proses layanan berdasarkan waktu dari konfigurasi
- Konfigurasi layanan melalui file JSON
- Unit & performance testing untuk semua modul

## Cara Menjalankan Test
```bash
#untuk menjalankan semua tests secara bersamaan
python -m unittest discover tests 

#menjalankan test spesifik
python -m unittest tests.test_queue #contoh jika ingin menjalankan test_queue.py 