# CONDITION (EF, ELIF, ELSE)

# nilai = int(input('Masukan Nilai siswa: '))
# if nilai > 80:
#     print('Exellent')
# elif nilai >= 60 and nilai <= 80:
#     print('Good job!')
# else:
#     print("Don't give up")

# LATIHAN
#Buat penentu angka ganjil & genap dari inputan

# nilai = int(input('Masukan Angka: '))
# if nilai % 2 == 0:
#     print(f'Angka {nilai} tergolong bilangan GENAP')
# else:
#     print(f'Angka {nilai} tergolong bilangan GANJIL')

#LATIHAN
# Tentukan IMT (massa(kg)/tinggi(meter)^2)
# a. IMT < 18.5 artinya berat badang kurang
# b. 18,5 - 24,9 artinya ideal
# c. 25,0 - 29,9 artinya BB berlebih
# b. 30,0 - 39,9 artinya BB sangat berlebih
# b. IMT > 39,9 artinya obesitas


# mssa = int(input('Masukan Massa(kg) : '))
# tggi = int(input('Masukan Tinggi(cm) : '))
# IMT = mssa /((tggi/100) ** 2)

# if IMT < 18.5:
#     print(f'Massa {mssa} & Tinggi {(tggi/100)}m')
#     print(f'IMT = {IMT}, Berat badan kurang')
# elif IMT > 18.5 and IMT <= 24.9:
#     print(f'Massa {mssa} & Tinggi {(tggi/100)}m')
#     print(f'IMT = {IMT}, Berat ideal')
# elif IMT > 25.0 and IMT <= 29.9:
#     print(f'Massa {mssa} & Tinggi {(tggi/100)}m')
#     print(f'IMT = {IMT}, Berat badan berlebih')
# elif IMT > 30.0 and IMT <= 39.9:
#     print(f'Massa {mssa} & Tinggi {(tggi/100)}m')
#     print(f'IMT = {IMT}, Berat badan sangat berlebih')
# else:
#     print(f'Massa {mssa} & Tinggi {(tggi/100)}m')
#     print(f'IMT = {IMT}, Obesitas')

#LATIHAN
#Jarak mobil A & B = 120km.
# A berjalan 60km/h dari timur
# B berjalan 40km/h dari barat
# A & B start pukul 9 WIB
# Jam brapa A & B bertabrakan?
#Rumus Jarak = Kecepatan X Waktu
#Rumus Waktu = Jarak Total / (Kec 1 + Kec 2)

# import math
# jarak = 120
# spdA = 60
# spdB = 40
# brgkt = 9

# waktu = jarak /(spdA+spdB)

# print(f'Akan bertabrakan pukul {(round(brgkt + waktu))}, lebih {(math.floor((waktu-1)*60))} Menit')

#LATIHAN
#Diketahui 485 hari, nyatakan dalan tahun, bulan, minggu, hari

import math
thn = 360
bln = 30
week = 4
print(f'485 Hari = {math.floor(485/thn)} tahun {math.floor((485 % thn)/bln)} bulan {(485 % thn) % bln} Hari')
print(f'485 Hari = {math.floor(485/thn)} tahun')
print(f'485 Hari = {math.floor(485/bln)} bulan')
print(f'485 Hari = {math.floor((485/30)*week)} minggu')



