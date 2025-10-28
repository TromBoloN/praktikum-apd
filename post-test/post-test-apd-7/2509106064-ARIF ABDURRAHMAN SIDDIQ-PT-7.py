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

templateData = {
    "users": ["username","password","role"],
    "dataMod" : ["nama","pembuat","update","versi","kompatibilitas"]
}

# Function login prosedur
def login():
    username = input("\nUsername: ")
    password = input("Password: ")

    if username == "" or password == "":
        input("\nUsername atau Password tidak boleh kosong. Tekan Enter...")
        return None

    if username in users and users[username]["password"] == password:
        print("\nLogin berhasil!")
        return users[username]["role"]
    else:
        input("\nLogin gagal. Tekan enter...")
        return None

# Function insert data ke dictionary terserah
def insertData(targetDict, tipeData):
    try:
        if tipeData not in templateData:
            print("Tipe Data tidak dikenal.")
            return

        dataBaru = {}
        print(f"\n=== Tambah {tipeData.upper()} ===")

        for i in templateData[tipeData]:
            value = input(f"Masukkan {i}: ").strip()

            if value == "":
                print(f"{i} tidak boleh kosong, diisi 'Tidak Diketahui'.")
                value = "Tidak Diketahui"

            elif i == "role":
                if value.lower() not in ["admin", "user"]:
                    print("Role tidak valid, default: user")
                    value = "user"

            dataBaru[i] = value

        if tipeData == "dataMod":
            keyBaru = max(targetDict.keys(), default=0) + 1
            targetDict[keyBaru] = dataBaru
            print("\nMod berhasil ditambahkan")

        elif tipeData == "users":
            username = dataBaru["username"]
            if username in targetDict:
                print("\nUsername sudah terdaftar.")
                return
            targetDict[username] = {
                "password": dataBaru["password"],
                "role": dataBaru["role"]
            }
            print("\nUser berhasil di registrasi")

        print("\nData Hasil Input:")
        for key, value in dataBaru.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"\nTerjadi kesalahan saat menambah data: {e}")

#Function baca data 1 per satu rekursif
def readData(tabel, listData, keys, value=0):
    if value == len(keys):
        return tabel
    
    idMod = keys[value]
    mod = listData[idMod]
    
    tabel.add_row([idMod, mod["nama"], mod["pembuat"], mod["update"], mod["versi"], mod["kompatibilitas"]])
    
    return readData(tabel, listData, keys, value + 1)
#Function lihat data dari function rekursif readData prosedur
def lihatListMod():  
    os.system('cls')
    print("=== DAFTAR MOD ===")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]

    tabel = readData(tabel, dataMod, list(dataMod.keys()))
    print(tabel)
#Function update data prosedur
def updateData():
    try:
        os.system('cls')
        print("=== UBAH MOD ===")
        lihatListMod()
        ubahMod = input("Masukkan nomor mod yang ingin diubah: ")
        if not ubahMod.isdigit() or int(ubahMod) not in dataMod:
            print("Nomor mod tidak valid.")
            return

        idMod = int(ubahMod)
        nama = input("Nama baru (kosongkan jika tidak diganti): ")
        pembuat = input("Pembuat baru (kosongkan jika tidak diganti): ")
        updateTerakhir = input("Update baru (YYYY-MM-DD): ")
        versiKompatibel = input("Versi baru (kosongkan jika tidak diganti): ")
        kompatibilitas = input("Kompatibilitas (Y/T): ").upper()

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
        print("Mod berhasil diubah!")

    except Exception as e:
        print(f"Terjadi error saat mengubah mod: {e}")
    


while True:
    os.system('cls')
    print("=== List Mod Victoria 3 ===")
    print("1. Login Admin")
    print("2. Login User")
    print("3. Register")
    print("4. Keluar")
    menuLogin = input("Pilih menu: ")

    if menuLogin == "1":
        role = login()

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
                    insertData(dataMod, "dataMod")
                    input("\nTekan Enter untuk lanjut...")

                elif menuMod == "2":
                    lihatListMod()
                    input("\nTekan Enter untuk kembali ke menu...")

                elif menuMod == "3":
                    updateData()
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
                input("Role tidak valid. Tekan Enter...")
                break
               
    elif menuLogin == "2":
            role = login()
            while True:
                os.system('cls')
                if role == "user":
                    print("1. Lihat List Mod")
                    print("2. Keluar")
                    menuUser = input("Pilih menu: ")

                    if menuUser == "1":
                        lihatListMod()
                        input("\nTekan Enter untuk kembali ke menu...")

                    elif menuUser == "2":
                        break
                    else:
                        input("Menu tidak valid. Tekan Enter...")
                else:
                    input("Role tidak valid. Tekan Enter...")
                    break
    
    elif menuLogin == "3":
        insertData(users, "users")
        input("\nTekan Enter untuk lanjut...")

    elif menuLogin == "4":
        os.system('cls')
        print("Keluar dari program...")
        break

    else:
        input("Menu tidak valid. Tekan Enter...")