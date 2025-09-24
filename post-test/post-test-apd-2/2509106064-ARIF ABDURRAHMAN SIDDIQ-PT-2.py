#POSTTEST 2 APD

#List suhu dan konversinya
suhu = [27,33,46,55,67,92]

suhu_1 = (suhu[0] * 9/5) + 32
suhu_2 = (suhu[1] * 9/5) + 32

suhu_3 = suhu[2] + 273.15
suhu_4 = suhu[3] + 273.15

suhu_5 = suhu[4] * 4/5
suhu_6 = suhu[5] * 4/5

#Jumlah tanpa sum, rata-rata, NIM, dan boolean NIM
jumlah_suhu = suhu_1 + suhu_2 + suhu_3 + suhu_4 + suhu_5 + suhu_6

rata_rata = jumlah_suhu / 6

NIM = 64

Bolean = NIM < rata_rata

#Print hasil
print(f"""
suhu_2 adalah         = {suhu_2}F
suhu_3 adalah         = {suhu_3}F
suhu_4 adalah         = {suhu_4}K 
suhu_5 adalah         = {suhu_5}K
suhu_1 adalah         = {suhu_1}R
suhu_6 adalah         = {suhu_6}R
Jumlah                = {jumlah_suhu}
Rata-rata             = {rata_rata}
NIM                   = {NIM}
Bolean                = {Bolean}
Slice index 46-92 (-) = {suhu[-4:]}
""")