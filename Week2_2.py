# FUNCTION
# Variable adalah tempat untuk menyimpan value (integer, string, float, list, dsb) yg diberi nama dan bisa dipakai lagi
# Function adalah tempat untuk menyimpan code yg diberi nama dan bisa dipakai lagi

# CONTOH FUNCTION DENGAN PARAMETER

# def segitiga(jumlah_bintang): # def NAMA_FUNCTION(PARAMETER), PARAMETER = hal ap yg perlu di input oleh user
#     teks = ''
#     for x in range(0,jumlah_bintang):
#         for y in range(0,x+1): 
#             teks +=(' * ')
#         teks += '\n'
#     print(teks)
# segitiga(5) #penggunaan function

# # CONTOH FUNCTION TANPA PARAMETER
# def Hallo():
#     print('Halooow')
# Hallo()

# CONTOH FUNCTION PENGALI
# def kalikan(a, b):
#     print(a * b)

# kalikan(3, 5)

#CONTOH FUNCTION DENGAN PARAMETER PART2
# def nama_lengkap(nama):
#     print(nama + ' Slamet')
# nama_lengkap('Andi')
# nama_lengkap('Budi')

#RETURN FUNCTION
# def total(x,y)
#     z = x + y
#     return z # Z jika tidak kita return maka hasilnya akan none

# print(total(4,5))
# print(z) # Z tidak bisa di print langsung karena Z adalah variable local(variable yg ada di dalam function)

#======================================================================================================================
# UPDATE PEMBELAJARAN

# DATA TYPES
# NUMBER : INTERGER, FLOAT => PENGOLAHANYA MENGGUNAKAN OPERASI MATEMATIKA SAJA
# STRING
# LIST
# DICTIONARY, SET, TUPLE

# TOOLS :
# 1. If Else (Condition)
# 2. Looping (Pengulangan)
# 3. Function (Penyimpanan Code)

#======================================================================================================================
# LIST = Variable yang berisi banyak value
# nama = 'Andi'
# umur = 34
# domisili = 'Bogor'

# # CONTOH LIST
# identias = ['Andi', 34, 'Bogor']

# buah = ['nanas', 'apel', 'jeruk', 'mangga', 'alpukat']

# # 1. INDEX (Untuk mengetahui posisi komponen di list)
# index_mangga = buah.index('mangga')
# #print(index_mangga)

# # 2. APPEND (Untuk menambah komponen di list)
# buah.append('salak') # menambah komponen salak
# buah.append('sawo') # menambah komponen sawo
# buah.append(['durian','rambutan']) # menambah list di dalam list
# # print(buah)
# # print(buah.index(['durian','rambutan']))

# # 3. INSERT (Untuk menambah komponen list di posisi index tertentu)
# buah.insert(0, 'pisang') #menambahkan komponen pisang di index ke - 0
# # print(buah)

# # 4. EXTEND (Untuk menambah komponen list ke dalam list tanpa menjadikan list baru di dalam list)
# buah.extend(['leci', 'manggis'])
# print(buah)

# 5. SLICING (Untuk mengakses komponen di dlam list) => formulanya adalah START => STOP =? STEP
# print(buah[1]) # nanas
# print(buah[0]) # pisang
# print(buah[8][0]) # mengakses komponen list di dalam list(durian ada di index ke - 8(berupa list dan durian berada di index ke - 0))
# print(buah[-1]) # mengakses komponen list secara terbalik(dari belakang)
# print(buah[::-1]) # mengakses semua komponen list secara terbalik(dari belakang ke depan)

# 6. REMOVE (Untuk menghapus komponen list secara spesifik)
#buah.remove('pisang') # menghapus pisang dari dalam list
#print(buah)

# 7. POP (Untuk menghapus komponen list secara spesifik by index no atau klo index no kosong akan menghapus komponen yg paling belakang)
# buah.pop()
# print(buah)

# 8. REVERSE (Untuk menampilkan komponen list secara terbalik(dari belakang ke depan))
#buah.reverse()
#print(buah)
#print(buah[::-1]) # bisa juga menggunakan perintah ini untuk menampilkan komponen list secara terbalik(dari belakang ke depan)

# 9. SORT (Untuk mengurutkan komponen list sesuai alfabet)
#buah.sort()
#print(buah)

# 10. COPY (Untuk mengcopy list jadi list baru dengan isi yang sama dengan list sebelumnya)
# fruit = buah.copy()
# print(fruit)

# LATIHAN
# mean, median, modus
# Buat function untuk menghitung salah satu central tendency

# import math
# data = [3, 50, 12, 34, 47, 87, 19, 37, 55, 3, 28]
# def mean(data):
#     a = math.floor(sum(data) / len(data))
#     return a
# print(mean(data))

# data = [3, 50, 12, 34, 47, 87, 19, 37, 55, 3, 28]

# import math
# def median(data):
#     data.sort()
#     if (sum(data)) % 2 == 0:
#         a = int(len(data)/2)
#         b = math.floor((data[a - 1] + data[a])/2)
#         return b
#     else:   
#         a = int((len(data)+1)/2)
#         b = data[a - 1]
#         return b
# # data.sort()
# # print(data)
# print(median(data))

data = [3, 50, 12, 34, 47, 87, 19, 37, 55, 3, 28, 50]
#def modus():
#     modus = max(set(data), key=data.count)
#     a = data.count(modus)
#     b = []
#     for i in data:
#         if a - 1 < data.count(i):
#             b.append(i)
#     c = b[::a]
#     modus1 = 'Modus data adalah '
#     modus2 = []
#     if len(c) == 1:
#         modus1 += str(c[0])
#     else:
#         for i in c:
#             modus2.append(str(i))
#         modus1 += ' & '.join(modus2)
    
#     print(modus)
#     return
# modus()
def modus():
    a = max(set(data), key=data.count)
    print(modus)
modus()
# import math
# def modus(data):
    



# =================================================================================================================
# LATIHAN
# BUATLAH ALGORITMA UNTUK MENGURUTKAN ELEMEN ARRAY BERIKUT
# X = [40,100,1,5,25,10]

# x = [40, 100, 1, 5, 25, 10]
# for i in range(10):
# #     print(f'Nomor urut {i+1}')

# if x[1] > x[2]:
#      x.insert(0,x[1])
#  elif nilai >= 60 and nilai <= 80:
#      print('Good job!')
#  else:
#      print("Don't give up")

#      buah.insert(0, 'pisang')