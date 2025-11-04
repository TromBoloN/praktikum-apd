from data import users, templateData

def login():
    username = input("\nUsername: ")
    password = input("Password: ")

    if not username or not password:
        input("\nUsername atau Password tidak boleh kosong. Tekan Enter...")
        return None

    if username in users and users[username]["password"] == password:
        print("\nLogin berhasil!")
        return users[username]["role"]

    input("\nLogin gagal. Tekan Enter...")
    return None


def register():
    dataBaru = {}
    print("\n=== Registrasi User ===")

    for i in templateData["users"]:
        value = input(f"Masukkan {i}: ").strip()
        if not value:
            print(f"{i} tidak boleh kosong, diisi 'Tidak Diketahui'.")
            value = "Tidak Diketahui"

        if i == "role" and value.lower() not in ["admin", "user"]:
            print("Role tidak valid, default: user")
            value = "user"

        dataBaru[i] = value

    username = dataBaru["username"]
    if username in users:
        print("\nUsername sudah terdaftar.")
        return

    users[username] = {
        "password": dataBaru["password"],
        "role": dataBaru["role"]
    }
    print("\nUser berhasil diregistrasi.")
