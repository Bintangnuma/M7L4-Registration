import sqlite3

DB_NAME = 'users.db'

def create_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_user(username, email, password):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate_user(username, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        return cursor.fetchone() is not None

def display_users():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, email FROM users')
        for user in cursor.fetchall():
            print(f"Nama Pengguna: {user[0]}, Email: {user[1]}")


def user_choice():
    print("\n1. Masuk")
    print("2. Daftar")
    choice = input("Silakan pilih menu (1/2): ")
    return choice

def main():
    create_db()
    display_users()  # Tampilkan daftar pengguna sebelum memilih tindakan

    choice = user_choice()

    if choice == '1':
        username = input("Masukkan nama pengguna: ")
        password = input("Masukkan kata sandi: ")
        if authenticate_user(username, password):
            print("Autentikasi berhasil.")
        else:
            print("Nama pengguna atau kata sandi salah.")
    elif choice == '2':
        username = input("Masukkan nama pengguna baru: ")
        email = input("Masukkan email pengguna baru: ")
        password = input("Masukkan kata sandi pengguna baru: ")
        add_user(username, email, password)
    else:
        print("Input tidak valid. Silakan masukkan 1 untuk masuk atau 2 untuk mendaftar.")

if __name__ == "__main__":
    main()
