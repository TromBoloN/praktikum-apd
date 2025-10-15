import os 
from prettytable import PrettyTable
os.system('cls')



users = [
    ["arif", "064", "admin"]
    ] 
dataMod = [
    ["Realistic Economy", "Victor Hugo", "2024-08-12", "1.5.3", "Kompatibel"],
    ["World Overhaul", "Marie Curie", "2024-06-25", "1.5.2", "Tidak Kompatibel"],
    ["Population Rework", "Arthur Conan", "2024-09-14", "1.5.3", "Kompatibel"]
]

# Loop Login
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
        testLogin = False
        role = ""
        
        for user in users:
            if user[0] == username and user[1] == password:
                testLogin = True
                role = user[2]
                break
            
        if not testLogin:
            if username == "" or password == "":
                input("Username atau Password tidak boleh kosong. Tekan Enter untuk lanjut...")
                continue
            else:
                input("Login gagal Tekan Enter untuk lanjut...")
                continue
         
        # Looping crudnya kalau berhasil login   
        while True:
            os.system('cls')
            print(f"===  MOD MENU {role.upper()} ===")
                
            if role == "admin":
                print("1. Tambah Mod")
                print("2. Lihat List Mod")
                print("3. Ubah Mod")
                print("4. Hapus Mod")
                print("5. Keluar")
                menuMod = input("Pilih menu: ")
                
                # Create mod
                if menuMod == "1":
                    nama = input("Nama Mod: ")
                    pembuat = input("Pembuat Mod: ")
                    updateTerakhir = input("Update Terakhir (YYYY-MM-DD): ")
                    versiKompatibel = input("Versi Kompatibel: ")
                    kompatibilitas = input("Kompatibilitas(Y/T): ").upper()
                    if kompatibilitas == "Y":
                        kompatibilitas = "Kompatibel"
                    elif kompatibilitas == "T":
                        kompatibilitas = "Tidak Kompatibel"
                    else:
                        input("\nTidak valid. Tekan Enter...")
                        continue
                    
                    dataMod.append([nama, pembuat, updateTerakhir, versiKompatibel, kompatibilitas])
                    input("\nMod berhasil ditambahkan! Tekan Enter...")
                    continue

                # Read mod
                elif menuMod == "2":
                    os.system('cls')
                    print("=== DAFTAR MOD ===")

                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]

                    for i, mod in enumerate(dataMod, start=1):
                        tabel.add_row([i, mod[0], mod[1], mod[2], mod[3], mod[4]])

                    print(tabel)
                    input("\nTekan Enter untuk kembali ke menu...")
                    continue
                
                # Update mod
                elif menuMod == "3":
                    os.system('cls')
                    
                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]

                    for i, mod in enumerate(dataMod, start=1):
                        tabel.add_row([i, mod[0], mod[1], mod[2], mod[3], mod[4]])

                    print(tabel)    
                    ubahMod = input("Masukkan nomor mod yang ingin diubah: ")
                    if ubahMod.isdigit():
                        idMod = int(ubahMod) - 1
                        if 0 <= idMod < len(dataMod):
                            nama = input("\nNama Mod baru (kosongkan jika tidak diganti): ")
                            pembuat = input("Pembuat Mod baru (kosongkan jika tidak diganti): ")
                            updateTerakhir = input("Update Terakhir baru (YYYY-MM-DD) (kosongkan jika tidak diganti): ")
                            versiKompatibel = input("Versi Kompatibel baru (kosongkan jika tidak diganti): ")
                            kompatibilitas = input("Kompatibilitas baru (Y/T) (kosongkan jika tidak diganti): ").upper()

                            if nama != "":
                                dataMod[idMod][0] = nama
                            if pembuat != "":
                                dataMod[idMod][1] = pembuat
                            if updateTerakhir != "":
                                dataMod[idMod][2] = updateTerakhir
                            if versiKompatibel != "":
                                dataMod[idMod][3] = versiKompatibel
                            if kompatibilitas == "Y":
                                dataMod[idMod][4] = "Kompatibel"
                            elif kompatibilitas == "T":
                                dataMod[idMod][4] = "Tidak Kompatibel"
                            elif kompatibilitas == "":
                                pass
                            else:
                                input("\nInput tidak valid. Tekan Enter...")
                                continue

                            input("\nMod berhasil diubah. Tekan Enter...")
                            continue
                        else:
                            input("\nNomor mod tidak ditemukan. Tekan Enter...")
                            continue
                    else:
                        input("\nInput tidak valid. Tekan Enter...")
                        continue

                # Delete mod
                elif menuMod == "4":
                    os.system('cls')
                    
                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]

                    for i, mod in enumerate(dataMod, start=1):
                        tabel.add_row([i, mod[0], mod[1], mod[2], mod[3], mod[4]])

                    print(tabel)
                    hapusMod = input("Masukkan nomor mod yang ingin dihapus: ")
                    if hapusMod.isdigit():
                        idMod = int(hapusMod) - 1
                        if 0 <= idMod < len(dataMod):
                            del dataMod[idMod]
                            input("\nMod berhasil dihapus. Tekan Enter...")
                            continue
                        else:
                            input("Nomor mod tidak ditemukan. Tekan Enter...")
                            continue
                    else:
                        input("\nInput tidak valid. Tekan Enter...")
                        continue
                 
                # Keluar        
                elif menuMod == "5":
                    break
                else:
                    input("\nMenu tidak valid. Tekan Enter...")
                    continue
            
            else:
                print("1. Lihat List Mod")
                print("2. Keluar")
                menuUser = input("Pilih menu: ")
                
                if menuUser == "1":
                    os.system('cls')
                    print("=== DAFTAR MOD ===")

                    tabel = PrettyTable()
                    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]

                    for i, mod in enumerate(dataMod, start=1):
                        tabel.add_row([i, mod[0], mod[1], mod[2], mod[3], mod[4]])

                    print(tabel)
                    input("\nTekan Enter untuk kembali ke menu...")
                    
                elif menuUser == "2":
                    break
                else:
                    input("\nMenu tidak valid. Tekan Enter...")
                    continue
    
    # Register user baru
    elif (menuLogin == "2"):
        os.system('cls')
        print("=== REGISTER USER BARU ===")
        usernameBaru = input("Masukkan username baru: ")
        passwordBaru = input("Masukkan password baru: ")
        roleBaru = "user"
        
        checkList = False
        for user in users:
            if user[0] == usernameBaru:
                checkList = True
                break

        if checkList:
            input("\nUsername sudah terdaftar. Tekan Enter untuk kembali...")
            continue
        if usernameBaru == "" or passwordBaru == "":
            input("\nUsername atau Password tidak boleh kosong. Tekan Enter untuk kembali...")
            continue
        else:
            users.append([usernameBaru, passwordBaru, roleBaru])
            input("\nRegistrasi berhasil. Tekan Enter untuk kembali...")
    
    # Keluar dari program
    elif (menuLogin == "3"):
        os.system('cls')
        print("\nKeluar dari program...")
        break
    
    else:
        input("\nMenu tidak valid. Tekan Enter untuk kembali...")
        continue