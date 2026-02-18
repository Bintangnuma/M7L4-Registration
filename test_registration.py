import pytest
import sqlite3
import os
from registration.registration import create_db, add_user, authenticate_user, display_users

@pytest.fixture(scope="module")
def setup_database():
    """Fixture untuk menyiapkan database sebelum pengujian dan membersihkannya setelah selesai."""
    create_db()
    yield
    try:
        os.remove('users.db')
    except PermissionError:
        pass

@pytest.fixture
def connection():
    """Fixture untuk mendapatkan koneksi database dan menutupnya setelah pengujian."""
    conn = sqlite3.connect('users.db')
    yield conn
    conn.close()


def test_create_db(setup_database, connection):
    """Menguji pembuatan database dan tabel pengguna."""
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    table_exists = cursor.fetchone()
    assert table_exists, "Tabel 'users' harus ada dalam database."

def test_add_new_user(setup_database, connection):
    """Menguji penambahan pengguna baru."""
    add_user('testuser', 'testuser@example.com', 'password123')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username='testuser';")
    user = cursor.fetchone()
    assert user, "Pengguna harus ditambahkan ke database."

# Berikut adalah pengujian yang bisa ditulis:
"""
Menguji percobaan menambahkan pengguna dengan nama pengguna yang sudah ada.
Menguji keberhasilan autentikasi pengguna.
Menguji autentikasi pengguna yang tidak ada.
Menguji autentikasi dengan kata sandi yang salah.
Menguji tampilan yang benar dari daftar pengguna.
"""

def test_add_existing_user(setup_database):
    """Menguji percobaan menambahkan pengguna dengan username yang sudah ada."""
    add_user('duplicateuser', 'dup@example.com', 'pass123')
    
    # Coba tambahkan lagi dengan username yang sama
    result = add_user('duplicateuser', 'dup2@example.com', 'pass456')
    
    # Sesuaikan dengan return function kamu
    # Misal function mengembalikan False jika gagal
    assert result is False, "Tidak boleh menambahkan username yang sudah ada."


def test_authenticate_user_success(setup_database):
    """Menguji keberhasilan autentikasi pengguna."""
    add_user('authuser', 'auth@example.com', 'securepass')
    
    result = authenticate_user('authuser', 'securepass')
    assert result is True, "Autentikasi harus berhasil dengan username dan password yang benar."


def test_authenticate_user_not_exist(setup_database):
    """Menguji autentikasi pengguna yang tidak ada."""
    result = authenticate_user('nonexistent', 'anypassword')
    assert result is False, "Autentikasi harus gagal jika user tidak ada."


def test_authenticate_user_wrong_password(setup_database):
    """Menguji autentikasi dengan password yang salah."""
    add_user('wrongpassuser', 'wp@example.com', 'correctpass')
    
    result = authenticate_user('wrongpassuser', 'wrongpass')
    assert result is False, "Autentikasi harus gagal jika password salah."


def test_display_users(setup_database, capsys):
    """Menguji tampilan yang benar dari daftar pengguna."""
    add_user('user1', 'user1@example.com', 'pass1')
    display_users()
    captured = capsys.readouterr()
    assert "user1" in captured.out


