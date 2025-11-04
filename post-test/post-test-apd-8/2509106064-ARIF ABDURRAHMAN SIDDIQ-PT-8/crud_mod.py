import os
from prettytable import PrettyTable
from data import dataMod, templateData
from datetime import date

def clear():
    os.system('cls')


def readData(tabel, listData, keys, value=0):
    if value == len(keys):
        return tabel

    idMod = keys[value]
    mod = listData[idMod]
    tabel.add_row([idMod, mod["nama"], mod["pembuat"], mod["update"], mod["versi"], mod["kompatibilitas"]])
    return readData(tabel, listData, keys, value + 1)


def lihatListMod():
    clear()
    print("=== DAFTAR MOD ===")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Mod", "Pembuat", "Update Terakhir", "Versi Kompatibel", "Kompatibilitas"]
    tabel = readData(tabel, dataMod, list(dataMod.keys()))
    print(tabel)


def insertData():
    try:
        dataBaru = {}
        print("\n=== Tambah MOD ===")

        for i in templateData["dataMod"]:
            value = input(f"Masukkan {i}: ").strip()
            if not value:
                print(f"{i} tidak boleh kosong, diisi 'Tidak Diketahui'.")
                value = "Tidak Diketahui"
            dataBaru[i] = value

        keyBaru = max(dataMod.keys(), default=0) + 1
        dataMod[keyBaru] = dataBaru
        print("\nMod berhasil ditambahkan.")

    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")


from datetime import date

def updateData():
    try:
        clear()
        print("=== UBAH MOD ===")
        lihatListMod()
        ubahMod = input("Masukkan nomor mod yang ingin diubah: ")
        if not ubahMod.isdigit() or int(ubahMod) not in dataMod:
            print("Nomor mod tidak valid.")
            return

        idMod = int(ubahMod)
        nama = input("Nama baru (kosongkan jika tidak diganti): ")
        pembuat = input("Pembuat baru (kosongkan jika tidak diganti): ")
        versiKompatibel = input("Versi baru (kosongkan jika tidak diganti): ")
        kompatibilitas = input("Kompatibilitas (Y/T): ").upper()

        if nama:
            dataMod[idMod]["nama"] = nama
        if pembuat:
            dataMod[idMod]["pembuat"] = pembuat
        if versiKompatibel:
            dataMod[idMod]["versi"] = versiKompatibel
        if kompatibilitas == "Y":
            dataMod[idMod]["kompatibilitas"] = "Kompatibel"
        elif kompatibilitas == "T":
            dataMod[idMod]["kompatibilitas"] = "Tidak Kompatibel"
            
        dataMod[idMod]["update"] = str(date.today())

        print(f"Mod berhasil diubah! (Update otomatis: {dataMod[idMod]['update']})")

    except Exception as e:
        print(f"Terjadi error saat mengubah mod: {e}")



def deleteData():
    clear()
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
