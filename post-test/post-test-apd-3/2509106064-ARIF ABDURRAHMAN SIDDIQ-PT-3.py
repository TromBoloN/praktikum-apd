# Login
username = "arif"
password = "064"

userInput = input("Masukkan Username: ")
passInput = input("Masukkan Password: ")

if userInput == username:
    if passInput == password:
        print("Anda berhasil login. Selamat datang", username)
    else:
        print("Password salah")
        exit()
else:
    if passInput == password:
        print("Username Salah")
        exit()
    else:
        print("Informasi login salah")
        exit()

#Kalkulator Konversi Satuan
tipeKalkulator = input("""
Tipe Kalkulator :   1. panjang  (Ke meter)
                    2. massa    (Ke Kilogram)
                    3. suhu     (Ke Kelvin)
                    4. waktu    (Ke Detik)
                    5. mata uang
Masukkan tipe kalkulator yang perlu dipakai :""")

#Kalkulator Panjang ke Meter
if tipeKalkulator == "panjang":
    tipePanjang = input("Masukkan Tipe panjang (Kaki(kaki), Kilometer(km), Centimeter(cm)):  ")
    nilai = float(input("Masukkan nilainya: "))
    if tipePanjang == "kaki":
        konversi = nilai * 0.3048
        print("Hasilnya = ", konversi ,"M")
    elif tipePanjang == "km":
        konversi = nilai * 1000
        print("Hasilnya = ", konversi ,"M")
    elif tipePanjang == "cm":
        konversi = nilai / 100
        print("Hasilnya = ", konversi ,"M")
    else:
        print("Tipe panjang tidak dikenal")

#Kalkulator Massa ke Kilogram      
elif tipeKalkulator == "massa":
    tipeMassa = input("Masukkan Tipe Massa (Pound(lbs), Ton(ton), Gram(g), Miligram(mg), Ounce(oz)):  ")
    nilai = float(input("Masukkan nilainya: "))
    if tipeMassa == "lbs":
        konversi = nilai * 0.453592
        print("Hasilnya = ", konversi ,"Kg")
    elif tipeMassa == "ton":
        konversi = nilai * 1000
        print("Hasilnya = ", konversi ,"Kg")
    elif tipeMassa == "g":
        konversi = nilai / 1000
        print("Hasilnya = ", konversi ,"Kg")
    elif tipeMassa == "mg":
        konversi = nilai / 1000000
        print("Hasilnya = ", konversi ,"Kg")
    elif tipeMassa == "oz":
        konversi = nilai * 0.0283495
        print("Hasilnya = ", konversi ,"Kg")
    else:
        print("Tipe massa tidak dikenal")

#Kalkulator Suhu ke Kelvin
elif tipeKalkulator == "suhu":
    tipeSuhu = input("Masukkan Tipe suhu (Celcius(c), Fahrenheit(f), Reamur(R)):  ")
    nilai = float(input("Masukkan nilainya: "))
    if tipeSuhu == "c":
        konversi = nilai + 273.15
        print("Hasilnya = ", konversi ,"K")
    elif tipeSuhu == "f":
        konversi = ((nilai - 32) * 5 / 9) + 273.15
        print("Hasilnya = ", konversi ,"K")
    elif tipeSuhu == "r":
        konversi = (nilai * 5 / 4) + 273.15
        print("Hasilnya = ", konversi ,"K")
    else:
        print("Tipe suhu tidak dikenal")

#Kalkulator Waktu ke Detik
elif tipeKalkulator == "waktu":
    tipeWaktu = input("Masukkan Tipe Waktu (menit(m), Jam(j)):  ")
    nilai = float(input("Masukkan nilainya: "))
    if tipeWaktu == "m":
        konversi = nilai * 60
        print("Hasilnya = ", konversi ," Detik")
    elif tipeWaktu == "j":
        konversi = nilai * 3600
        print("Hasilnya = ", konversi ," Detik")
    else:
        print("Tipe Waktu tidak dikenal")

#Kalkulator Mata Uang ke Dollar, Euro, Yen, dan Rupiah     
elif tipeKalkulator == "mata uang":
    tipeMataUang = input("Masukkan Tipe Mata Uang (Dollar(D), Euro(E), Yen(Y)):  ")
    nilai = float(input("Masukkan nilainya: "))
    if tipeMataUang == "D":
        tipeKonversiUang = input("Konversi ke Euro (E), Rupiah (R), atau Yen (Y)? ")
        if tipeKonversiUang == "E":
            konversi = nilai * 0.85
            print("Hasilnya = ", konversi ," EUR")
        elif tipeKonversiUang == "R":
            konversi = nilai * 15000
            print("Hasilnya = ", konversi ," IDR")
        elif tipeKonversiUang == "Y":
            konversi = nilai * 110
            print("Hasilnya = ", konversi ," JPY")
        else:
            print("Tipe Mata Uang tidak dikenal")

    elif tipeMataUang == "E":
        tipeKonversiUang = input("Konversi ke Dollar(D), Rupiah(R), atau Yen(Y)? ")
        if tipeKonversiUang == "D":
            konversi = nilai * 1.18
            print("Hasilnya = ", konversi ," USD")
        elif tipeKonversiUang == "R":
            konversi = nilai * 17000
            print("Hasilnya = ", konversi ," IDR")
        elif tipeKonversiUang == "Y":
            konversi = nilai * 129
            print("Hasilnya = ", konversi ," JPY")
        else:
            print("Tipe Mata Uang tidak dikenal")
            
    elif tipeMataUang == "Y":
        tipeKonversiUang = input("Konversi ke Dollar(D), Rupiah(R), atau EURO(E)? ")
        if tipeKonversiUang == "D":
            konversi = nilai * 0.0091
            print("Hasilnya = ", konversi ," USD")
        elif tipeKonversiUang == "R":
            konversi = nilai * 130
            print("Hasilnya = ", konversi ," IDR")
        elif tipeKonversiUang == "E":
            konversi = nilai * 0.0077
            print("Hasilnya = ", konversi ," EUR")
        else:
            print("Tipe Mata Uang tidak dikenal")
else:
    print("Tipe data tidak dikenal")