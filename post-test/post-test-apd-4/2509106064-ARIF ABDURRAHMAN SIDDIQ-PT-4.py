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

#Input golongan dan volume darah

aPos = 0
aNeg = 0
bPos = 0
bNeg = 0
abPos = 0
abNeg = 0
oPos = 0
oNeg = 0

while True:
    darah = input("\nMasukkan golongan darah (A, B, AB, O): ").strip().upper()

    if darah == "":
        print("Golongan darah tidak boleh kosong")
        continue
    elif darah == "A" or darah == "B" or darah == "AB" or darah == "O":
        pass  # valid
    else:
        print("Golongan darah tidak valid")
        continue

    rhesus = input("Masukkan Rhesus (+ atau -): ").strip()

    if rhesus == "":
        print("Rhesus tidak boleh kosong")
        continue
    elif rhesus == "+" or rhesus == "-":
        pass
    else:
        print("Rhesus tidak valid")
        continue

    print(f"Golongan darah Anda: {darah}{rhesus}")

    print("\n" + g40)
    kantongDarahStr = input("\nMasukkan jumlah kantong: ").strip()

    if kantongDarahStr == "":
        print("Jumlah kantong darah tidak boleh kosong")
        continue
    elif not kantongDarahStr.isdigit():
        print("Jumlah kantong darah harus berupa angka")
        continue
    else:
        kantongDarah = int(kantongDarahStr)
        if kantongDarah <= 0:
            print("Kantong darah harus lebih dari 0")
            continue

    volumeDarah = kantongDarah * 500

    if darah == "A" and rhesus == "+":
        aPos += volumeDarah
    elif darah == "A" and rhesus == "-":
        aNeg += volumeDarah
    elif darah == "B" and rhesus == "+":
        bPos += volumeDarah
    elif darah == "B" and rhesus == "-":
        bNeg += volumeDarah
    elif darah == "AB" and rhesus == "+":
        abPos += volumeDarah
    elif darah == "AB" and rhesus == "-":
        abNeg += volumeDarah
    elif darah == "O" and rhesus == "+":
        oPos += volumeDarah
    elif darah == "O" and rhesus == "-":
        oNeg += volumeDarah

    inputLagi = input("Apakah Anda ingin memasukkan data lagi? (Y/T): ").upper()
    if inputLagi == "":
        print("Input tidak boleh kosong, program akan berhenti.")
        break
    elif inputLagi == "T":
        break
    elif inputLagi != "Y":
        print("Input tidak valid, program akan berhenti.")
        break

#Hasil

print("\n" + g40)
print("\nData Golongan Darah dan Volume Darah yang Dimasukkan: \n")
print(g40)

if aPos > 0:
    print(f"Golongan Darah A+ : {aPos} ml")
if aNeg > 0:
    print(f"Golongan Darah A- : {aNeg} ml")
if bPos > 0:
    print(f"Golongan Darah B+ : {bPos} ml")
if bNeg > 0:
    print(f"Golongan Darah B- : {bNeg} ml")
if abPos > 0:
    print(f"Golongan Darah AB+ : {abPos} ml")
if abNeg > 0:
    print(f"Golongan Darah AB- : {abNeg} ml")
if oPos > 0:
    print(f"Golongan Darah O+ : {oPos} ml")
if oNeg > 0:
    print(f"Golongan Darah O- : {oNeg} ml")

print(g40)
