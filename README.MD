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

# CLO4_TB_KPL - Design Pattern and Clean Code Implementation

## Deskripsi
Pengimplementasian Design Pattern dan Clean Code ke dalam codebase dalam rangka memenuhi tugas besar CLO4 mata perkuliahan Konstruksi Perangkat Lunak

## Hasil Implementasi
- Strategy Pattern dalam modules/simulator.py
- Facade Pattern dalam modules/app_facade.py
- Implementasi prinsip clean code seperti python naming convention, dan type hinting
- Unittest dengan Coverage, dan Memory Profiling

## Cara Menjalankan Aplikasi

### - Membuat virtual environment (dianjurkan)
```bash
python -m venv nama-venv
```
### - Aktifkan virtual environment (jika membuat)
```bash
# Jika memakai CMD
nama-venv\Scripts\activate

# Jika memakai powershell
nama-venv\Scripts\Activate.ps1
```

### - Instal package dependency
```bash
pip install -r requirements.txt
```
### - Run main
```bash
python main.py
```

## Cara Menjalankan Test
```bash
#untuk menjalankan semua tests secara bersamaan
python -m unittest discover tests 
```
```bash
#menjalankan test spesifik
#contoh jika ingin menjalankan test_registration.py
python -m unittest tests.test_registration
```
## Cara Menjalankan Performance Profiling
```bash
python profile_runner.py
```
## Cara Menampilkan Coverage Unittest
```bash
# Untuk report CLI
coverage report

# Dalam bentuk html
coverage html
.\htmlcov\index.html
```