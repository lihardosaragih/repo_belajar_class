# print('Hello Word')

#VARIABLE
#Variable : Variables are named values and can store any type of value

# nama_saya = 'Dods'
# print(nama_saya)

#Data Types
#Dictionary :{'Nama': 'Andi','Umur': 22, 'Profes': 'Guru'}

#Cara Cek Data Type
# nama = 'Dods'
# umur = 22
# tinggi = 168.5
# jomblo = False

# print(type(nama))
# print(type(jomblo))
# print(type(tinggi))

#LATIHAN 1
# nama = input('Nama kamu ?')
# umur = input('Umur kamu ?')
# kelamin = input('Kelamin kamu ?')
# pekerjaan = input('Pekerjaan kamu ?')

# print('Nama : ',nama)
# print('Umur : ',umur)
# print('Kelamin : ', kelamin)
# print('Pekerjaan : ', pekerjaan)

#NUMBERS & ARITMETIC OPERATORS
# % => Modulus (sisa pembagian)

# usiaAndi = 40
# usiaBudi = 20

# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi) #penggunaan modulus
# print(usiaBudi ** 2)#penggunaan pangkat

# usiaAndi += 5
#usiaAndi = usiaAndi + 5

# usiaBudi -= 10
#usiaAndi - usiaBudi - 10
#Bisa dibilang penyederhanaan oparasi aritmatika
#dst

#LATIHAN APLIKASI PENGHITUNG LUAS PERSEGI PANJANG
# panjang = int(input('Masukan Panjang : '))#dirubah dari string ke int
# lebar = int(input('Masukan Lebar : '))#dirubah dari string ke int
# luas = panjang * lebar

# print('Luas Persegi Panjang : ',luas)
  
#MATH MODULE
# import math

# print(math.pi) #mencari angka pi
# print(math.fabs(-100))#fabs(float absolute) untuk mengabsolutkan angka
# print(math.pow(8, 2))#pangkat(8 pangkat 2)
# print(math.sqrt(49))#mencari akar kuadrat
# print(math.floor(4.7))#untuk membulatkan kebawah
# print(math.ceil(4.1))#untuk membulatkan keatas
# print(round(4.7))#membulatkan sesuai aturan matematika(function bawaan phytn)
# print(round(4.1))#membulatkan sesuai aturan matematika(function bawaan phytn)

#LATIHAN 3
#Jumlah usia andi 49th, dengan rasio usia andi & budi = 0.4
#Berapa usia Andi & Budi 2 tahun lagi?
#rasio 0.4 = Andi = 4, Budi = 10

# rasio_andi = 4
# rasio_budi = 10
# total_rasio = rasio_andi + rasio_budi
# total_umur = 49

# umur_andi = rasio_andi / total_rasio * total_umur
# umur_budi = rasio_budi / total_rasio * total_umur

# tambahan_umur = 2
# umur_andi_kedepan = umur_andi + tambahan_umur
# umur_budi_kedepan = umur_budi + tambahan_umur
# print(round(umur_andi_kedepan))
# print(round(umur_budi_kedepan))

# STRING
#teks = 'Mari kita belajar data science'

# print(len(teks))#length
# print(teks.index('data'))#mengetahui posisi index
# print(teks.split(' '))#memisahkan teks berdasarkan spasi/output yg muncul seperti function list
# print(teks.capitalize())
# print(teks.upper())
# print(teks.lower())

#STRING INDEXING
#[start:stop:step]start = awal, stop = akhir, step :lompatan pengambilan karakter
# print(teks[0])
# print(teks[2:])
# print(teks[0:30:1])
# print(teks[0:30:2])
# print(teks[:5])#start from beginning until 5 => 0,1,2,3,4
# print(teks[::2])#start from beginning, stop until end, step every 2
# print(teks[::-2])#step minus artinya terbalik

# CONVERT STRING TO NUMBER
# panjang = input('Masukan besaran panjang: ')
# lebar = input('Masukan besaran lebar: ')

# print(int(panjang) + int(lebar)) #sudah dikonversi ke integer
# print(float(panjang) + float(lebar)) #sudah dikonversi ke float

# usia = 22
# nama = 'Andi'
# print(usia + usia)
# print(str(usia))

#LATIAN
#Silahkan masukan angka berapapun ex : 4
#Kuadrat dari 4 = 6

# angka = int(input('Masukan Angka : '))
# kuadrat = angka **2
# print(f'Kuadrat dari {angka} adalah {kuadrat} ') #f = format, bermanfaat untuk menyisipkan variabel di dlm string

# LATIHAN
# Perusahaan Sehat Sentosa memiliki 3 cabang pabrik yaitu di bandung, semarang, dan surabaya
# Setiap cabang memiliki 3 jenis mesin penghasil masker yaitu mesin A, B, C
# Kapasitas produksi mesin A: 500 masker/hari, mesin B: 300 masker/hari, mesin C: 100 masker/hari
# Semua cabang memiliki 3 jenis mesin, kecuali Semarang (Mesin B)
# Berapa produksi perusahaan Sehat Sentosa selama 1 bulan (30 Hari)

msnA = 500
msnB = 300
msnC = 100

ttlProdSMG = msnA + msnC
ttlProdBDG = msnA + msnB + msnC
ttlProdSBY = msnA + msnB + msnC

ttlProdSbln = (ttlProdBDG + ttlProdSBY + ttlProdSMG)* 30

print(f'Jadi Total Produksi Masker Perusahaan Sehat Sentosa selama 1 bulan adalah : {ttlProdSbln}')

