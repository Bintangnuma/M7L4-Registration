# User Management System

Sistem manajemen pengguna sederhana yang diimplementasikan menggunakan Python. Sistem ini menggunakan SQLite untuk penyimpanan data pengguna. Program ini memungkinkan penambahan pengguna baru, autentikasi pengguna yang sudah ada, dan menampilkan daftar semua pengguna yang terdaftar.

## Fitur

- **Menambahkan pengguna baru**: Aplikasi menyimpan data login pengguna baru ke dalam database
- **Autentikasi pengguna**: Aplikasi memverifikasi kredensial pengguna sebelum autentikasi
- **Menampilkan daftar pengguna**: Aplikasi menampilkan daftar semua pengguna beserta datanya (tidak termasuk kata sandi)

## Memulai

Untuk menggunakan program ini, pastikan Anda memiliki Python versi 3.6 atau lebih tinggi dan SQLite terinstal.

### Instalasi

1. Clone repositori ke komputer lokal Anda:
    ```bash
    git clone repository_path
    ```
2. Masuk ke direktori proyek:
    ```bash
    cd User_Management_System_DB
    ```

### Penggunaan

Untuk menjalankan program, eksekusi perintah berikut di terminal Anda:
```bash
python registration.py
```
Ikuti petunjuk yang muncul di layar untuk mengelola pengguna.

### Pengujian

Program ini menyertakan unit test yang ditulis menggunakan library pytest. Untuk menjalankan test, pastikan pytest sudah terinstal (instal melalui pip jika diperlukan):
```bash
pip install pytest
```

Jalankan test dari direktori utama proyek dengan perintah berikut:
```bash
pytest
```

