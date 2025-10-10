# Login 
username = "arif"
password = "064"
g40 = "="*100

print(g40)
print("\nMasukkan Informasi Login")

while True:
    u = input("\nMasukkan username: ").strip()
    p = input("Masukkan password: ").strip()

    if u == "" and p == "":
        print("Username dan Password tidak boleh kosong")
    elif u == "":
        print("Username tidak boleh kosong")
    elif p == "":
        print("Password tidak boleh kosong")
    elif u != username and p != password:
        print("User tidak dikenal")
    elif u != username:
        print("Username salah")
    elif p != password:
        print("Password salah")
    else:
        print("Login berhasil!")
        break
    
print(f"\nSelamat Datang {username}\n")
print(g40)

# Golongan dan Volume Darah
golonganData = []
volumeData = []

darahValid = ["A", "B", "AB", "O"]
rhesusValid = ["+", "-"]

while True:
    darah = input("\nMasukkan golongan darah (A, B, AB, O): ").strip().upper()

    if darah == "":
        print("Golongan darah tidak boleh kosong!")
        continue
    elif darah not in darahValid:
        print("Golongan darah tidak valid!")
        continue
    else:
        rhesus = input("Masukkan Rhesus (+ atau -): ").strip()
        if rhesus == "":
            print("Rhesus tidak boleh kosong!")
            continue
        elif rhesus not in rhesusValid:
            print("Rhesus tidak valid!")
            continue
        else:
            print(f"Golongan darah Anda: {darah}{rhesus}")
            
        
    print("\n" + g40)

    kantongDarahStr = input("\nMasukkan jumlah kantong: ").strip()

    if kantongDarahStr == "":
        print("Jumlah kantong darah tidak boleh kosong!")
        continue
    else:
        kantongDarah = int(kantongDarahStr)
        if kantongDarah <= 0:
            print("Jumlah kantong darah harus lebih dari 0!")
            continue
        else:
            volumeDarah = kantongDarah * 500


    golonganData.append(darah + rhesus)
    volumeData.append(volumeDarah)

    inputLagi = input("Apakah Anda ingin memasukkan data lagi? (Y/T): ").upper()
    if inputLagi == "":
        print("Input tidak boleh kosong, program akan berhenti.")
        break
    elif inputLagi == "T":
        break
    elif inputLagi != "Y":
        print("Input tidak valid, program akan berhenti.")
        break

print("\n" + g40)
print("\nData Golongan Darah dan Volume Darah yang Dimasukkan: \n")
print(g40)

# Print listnya
golonganList = []
for i in range(len(golonganData)):
    gol = golonganData[i]
    if gol not in golonganList:
        golonganList.append(gol)
        total = 0
        for j in range(len(golonganData)):
            if golonganData[j] == gol:
                total += volumeData[j]
        print(f"Golongan Darah {gol} : {total} ml")

print("="*40)