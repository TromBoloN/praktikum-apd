import os
from auth import login, register
from crud_mod import lihatListMod, insertData, updateData, deleteData, clear


while True:
    clear()
    print("=== List Mod Victoria 3 ===")
    print("1. Login Admin")
    print("2. Login User")
    print("3. Register")
    print("4. Keluar")
    menuLogin = input("Pilih menu: ")

    if menuLogin == "1":
        role = login()
        if not role:
            continue

        if role != "admin":
            input("Anda bukan admin. Tekan Enter...")
            continue

        while True:
            clear()
            print(f"===  MOD MENU ({role.upper()}) ===")
            print("1. Tambah Mod")
            print("2. Lihat List Mod")
            print("3. Ubah Mod")
            print("4. Hapus Mod")
            print("5. Keluar")
            menuMod = input("Pilih menu: ")

            if menuMod == "1":
                insertData()
                input("\nTekan Enter untuk lanjut...")

            elif menuMod == "2":
                lihatListMod()
                input("\nTekan Enter untuk kembali ke menu...")

            elif menuMod == "3":
                updateData()
                input("\nTekan Enter untuk lanjut...")

            elif menuMod == "4":
                deleteData()

            elif menuMod == "5":
                break
            else:
                input("Menu tidak valid. Tekan Enter...")

    elif menuLogin == "2":
        role = login()
        if not role or role != "user":
            input("Role tidak valid. Tekan Enter...")
            continue

        while True:
            clear()
            print("=== USER MENU ===")
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

    elif menuLogin == "3":
        register()
        input("\nTekan Enter untuk lanjut...")

    elif menuLogin == "4":
        clear()
        print("Keluar dari program...")
        break

    else:
        input("Menu tidak valid. Tekan Enter...")
