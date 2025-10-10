# ulangi = 10
# for a in range(ulangi):
#     print(f"Hello World ke {a}")
    
# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)
    
# for i in range(1, 10):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
# print('') 

# tanya = 'y'
# hitung = 0
# while(tanya == 'y'):
#     hitung += 1
#     tanya = input("Ulang lagi? (y/n) ")
# print(f"Total perulangan: {hitung}")

# angka = 84
# print("Mencari angka pertama yang lebih besar dari 10...")
# for n in range(angka):
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")

# for i in range(10):
#     for j in range(i):
#         print(i , end='')
#     print(' =', i * i)
# print("")

# for i in range(10):
#     for j in range(i):
#         print(i , end=' ')
#     print(' =', i * i)
# print("")

n = 10

print("*", end="\t")
for i in range(1, n + 1):
    print(i, end="\t")
print()

for i in range(1, n + 1):
    print(i, end="\t") 
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()


# for i in range(8, 0, -1):
#     for j in range(i):*
#         print(i , end='')
#     print()
# print("")
# dompet = [1000,2000,3000,4000]
# for i in dompet:
#     print(i)

# tinggi = int(input("masukkan tinggi segitiga"))

# for i in range(tinggi):
#     # Cetak spasi
#     for j in range(tinggi - i - 1):
#         print(" ", end="")
#     # Cetak bintang
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print() 
    
# tinggi = int(input("masukkan tinggi segitiga"))

# for i in range of 


# fani = int(input("Masukkan jarak hari Fani: "))
# fatin = int(input("Masukkan jarak hari Fatin: "))

# hari = 1
# while True:
#     hari += 1
#     if hari % fani == 0 and hari % fatin :
#         print(f"Mereka ketemu jadi caster di hari ke {hari}")
#         break

# angka = [2, 5, 8, 12, 15, 7, 20]
# print("Mencari angka pertama yang lebih besar dari 10...")
# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")

# fani = int(input("Masukkan jarak hari Fani: "))
# fatin = int(input("Masukkan jarak hari Fatin: "))

# hari = 1
# while True:
#     if hari % fani == 0 and hari % fatin == 0:
#         print(f"Mereka ketemu jadi caster di hari ke {hari}")
#         break
#     hari += 1


# username = "a"

# userInput = input("Masukkan username")
# while True:
#     if userInput != username:
#         userInput = input("Masukkan username: ")
#     else:
#         print("Halo selamat datang")
#         break