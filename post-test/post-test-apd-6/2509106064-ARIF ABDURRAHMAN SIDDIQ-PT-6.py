import os
from prettytable import PrettyTable
os.system('cls')

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "arif": {"password": "064", "role": "user"}
}

dataMod = {
    1: {
        "nama": "Realistic Economy",
        "pembuat": "Victor Hugo",
        "update": "2024-08-12",
        "versi": "1.5.3",
        "kompatibilitas": "Kompatibel"
    },
    2: {
        "nama": "World Overhaul",
        "pembuat": "Marie Curie",
        "update": "2024-06-25",
        "versi": "1.5.2",
        "kompatibilitas": "Tidak Kompatibel"
    },
    3: {
        "nama": "Population Rework",
        "pembuat": "Arthur Conan",
        "update": "2024-09-14",
        "versi": "1.5.3",
        "kompatibilitas": "Kompatibel"
    }
}

while True:
    os.system('cls')
    print("=== List Mod Victoria 3 ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menuLogin = input("Pilih menu: ")

    if menuLogin == "1":
        username = input("\nUsername: ")
        password = input("Password: ")

        if username == "" or password == "":
            input("Username atau Password tidak boleh kosong. Tekan Enter...")
            continue

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
        else:
            input("Login gagal. Tekan Enter untuk lanjut...")
            continue

        while True:
            os.system('cls')
            print(f"===  MOD MENU ({role.upper()}) ===")

            if role == "admin":
                print("1. Tambah Mod")
                print("2. Lihat List Mod")
                print("3. Ubah Mod")
                print("4. Hapus Mod")
                print("5. Keluar")
                menuMod = input("Pilih menu: ")

                if menuMod == "1":
                    nama = input("\nNama Mod: ")
                    pembuat = input("Pembuat Mod: ")
                    updateTerakhir = input("Update Terakhir (YYYY-MM-DD): ")
                    versiKompatibel = input("Versi Kompatibel: ")
                    kompatibilitas = input("Kompatibilitas (Y/T): ").upper()

                    if kompatibilitas == "Y":
                        kompatibilitas = "Kompatibel"
                    elif kompatibilitas == "T":
                        kompatibilitas = "Tidak Kompatibel"
                    else:
                        input("\nInput tidak valid. Tekan Enter...")
                        continue

                    next_id = max(dataMod.keys(), default=0) + 1
                    dataMod[next_id] = {
                        "nama": nama,
                        "pembuat": pembuat,
                        "update": updateTerakhir,
                        "versi": versiKompatibel,
                        "kompatibilitas": kompatibilitas
                    }

                    input("\nMod berhasil ditambahkan! Tekan Enter...")

                elif menuMod == "2":
                    os.system('cls')
                    print("=== DAFTAR MOD ===")
                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]

                    for i, (idMod, mod) in enumerate(dataMod.items(), start=1):
                        tabel.add_row([idMod, mod["nama"], mod["pembuat"], mod["update"], mod["versi"], mod["kompatibilitas"]])

                    print(tabel)
                    input("\nTekan Enter untuk kembali ke menu...")

                elif menuMod == "3":
                    os.system('cls')
                    print("=== UBAH MOD ===")
                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]
                    for idMod, mod in dataMod.items():
                        tabel.add_row([idMod, mod["nama"], mod["pembuat"], mod["update"], mod["versi"], mod["kompatibilitas"]])
                    print(tabel)

                    ubahMod = input("Masukkan nomor mod yang ingin diubah: ")
                    if not ubahMod.isdigit() or int(ubahMod) not in dataMod:
                        input("Nomor mod tidak valid. Tekan Enter...")
                        continue

                    idMod = int(ubahMod)
                    nama = input("Nama Mod baru (kosongkan jika tidak diganti): ")
                    pembuat = input("Pembuat Mod baru (kosongkan jika tidak diganti): ")
                    updateTerakhir = input("Update Terakhir baru (YYYY-MM-DD): ")
                    versiKompatibel = input("Versi Kompatibel baru (kosongkan jika tidak diganti): ")
                    kompatibilitas = input("Kompatibilitas baru (Y/T) (kosongkan jika tidak diganti): ").upper()

                    if nama:
                        dataMod[idMod]["nama"] = nama
                    if pembuat:
                        dataMod[idMod]["pembuat"] = pembuat
                    if updateTerakhir:
                        dataMod[idMod]["update"] = updateTerakhir
                    if versiKompatibel:
                        dataMod[idMod]["versi"] = versiKompatibel
                    if kompatibilitas == "Y":
                        dataMod[idMod]["kompatibilitas"] = "Kompatibel"
                    elif kompatibilitas == "T":
                        dataMod[idMod]["kompatibilitas"] = "Tidak Kompatibel"
                    elif kompatibilitas != "":
                        input("Input tidak valid. Tekan Enter...")
                        continue

                    input("\nMod berhasil diubah! Tekan Enter...")

                elif menuMod == "4":
                    os.system('cls')
                    print("=== HAPUS MOD ===")
                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]
                    for idMod, mod in dataMod.items():
                        tabel.add_row([idMod, mod["nama"], mod["pembuat"], mod["update"], mod["versi"], mod["kompatibilitas"]])
                    print(tabel)

                    hapusMod = input("Masukkan nomor mod yang ingin dihapus: ")
                    if hapusMod.isdigit() and int(hapusMod) in dataMod:
                        del dataMod[int(hapusMod)]
                        input("Mod berhasil dihapus! Tekan Enter...")
                    else:
                        input("Nomor mod tidak ditemukan. Tekan Enter...")

                elif menuMod == "5":
                    break
                else:
                    input("Menu tidak valid. Tekan Enter...")

            else:
                print("1. Lihat List Mod")
                print("2. Keluar")
                menuUser = input("Pilih menu: ")

                if menuUser == "1":
                    os.system('cls')
                    print("=== DAFTAR MOD ===")
                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]

                    for i, (idMod, mod) in enumerate(dataMod.items(), start=1):
                        tabel.add_row([idMod, mod["nama"], mod["pembuat"], mod["update"], mod["versi"], mod["kompatibilitas"]])

                    print(tabel)
                    input("\nTekan Enter untuk kembali ke menu...")

                elif menuUser == "2":
                    break
                else:
                    input("Menu tidak valid. Tekan Enter...")

    elif menuLogin == "2":
        os.system('cls')
        usernameBaru = input("Masukkan username baru: ")
        passwordBaru = input("Masukkan password baru: ")
        roleBaru = input("Masukkan role (admin/user): ").lower()

        if usernameBaru == "" or passwordBaru == "":
            input("Username atau Password tidak boleh kosong. Tekan Enter...")
            continue

        if usernameBaru in users:
            input("Username sudah terdaftar. Tekan Enter...")
            continue
        if roleBaru not in ["admin", "user"]:
            input("Role tidak valid. Tekan Enter...")
            continue

        users[usernameBaru] = {"password": passwordBaru, "role": roleBaru}
        input("Registrasi berhasil! Tekan Enter...")

    elif menuLogin == "3":
        os.system('cls')
        print("Keluar dari program...")
        break

    else:
        input("Menu tidak valid. Tekan Enter...")
