# FUNCTION = Kumpulan/simpanan code yg diberi nama dan bisa dipakai lagi

# ===================================================================================
# STRING = data type yg memiliki tanda '' atau ""

# teks = "Learn From Home"

# 1. UPPER: Mengubah semua karakter menjadi huruf kapital / besar
#print(teks.upper())

# 2. LOWER:Mengubah semua karakter menjadi huruf kecil
#print(teks.lower())

# 3. CAPITALIZE: Mengubah karakter awal menjadi huruf kapital / besar
#print(teks.capitalize())

# 4. JOIN: Menambah suatu karakter ke dalam string
# strip = '-'
# new_teks = strip.join(teks)
# grup = ['Andi','Budi','Caca']
# koma = ','
# print(new_teks)
# print(koma.join(grup))

# 5. REPLACE: Mengganti karakter di dalam string
# print(teks.replace('Learn', 'Belajar'))
# newTeks = 'Belajar dari rumah'
# print(teks.replace(teks, newTeks))
# print(teks.replace('From',''))

# 6. SPLIT : Memisahkan karakter di dalam string berdasarkan karakter tertentu
#            sehingga berubah menjadi list
# print(teks.split(' ')) # dipisah berdasarkan spasi
# hasil = teks.split(' ')
# print(type(hasil)) # mengecek data type
# print(teks.split('a'))

# 7. COUNT: Menghitung jumlah karakter
# print(teks.count('a'))
# print(teks.count('o'))

# ===========================================================================================
# LATIHAN

#teks = 'Belajar Data Science di Purwadhika'

# 1. 1. Buat function seperti count yg bisa menghitung jumlah suatu huruf atau karakter
#hitung_huruf('a')
# 2. Buat function untuk menghitung jumlah kata dalam string
#hitung_kata()
# 3. Buat function untuk membalikkan urutan dalam string
# 'Purwadhika di Sciende Data Belajar'

# 1
# def hitung_huruf(karakter,yourText):
#     panjang = len(yourText)
#     hitung = 0

#     for i in range(0, panjang):
#         if yourText[i] == karakter:
#             hitung += 1
#     return (f'jumlah huruf {karakter} adalah {hitung}')
# print(hitung_huruf('B',teks))


# 2
# def hitung_kata(yourText):
#     kata = yourText.split(' ')
#     print(len(kata))
# hitung_kata(teks)

# 3
# def balik_kata(yourText):
#     spasi = ' '
#     kata = yourText.split(' ')
#     newTeks = spasi.join(kata[::-1])
#     print(newTeks)
# balik_kata(teks)

# =======================================================================
# FUNCTION TANPA NAMA & SEKALI PAKAI (LAMDA FUNCTION)
# MAP adalah untuk menjalankan sebuah fungsi terhadap banyak nilai masukan / data sekaligus.

# gaji = [1,2,3,4,5,6,7,8,9,10,15,20]

# # dengan function normal/biasa
# def pajak(yourList):
#     return yourList * 0.1

# # Menjalankan function di dalam variable
# # membuat variable dengan nama list_pajak
# list_pajak = list(map(pajak, gaji)) # Membuat list(menjalankan function(pajak) pada data (gaji))
# print(list_pajak)

# # Bandingkan function diatas dengan function tanpa nama & sekali pakai (lamda function)
# list_pajak_lambda = list(map(lambda yourList: yourList * 0.1,gaji))
# print(list_pajak_lambda)

# LATIHAN
# BUAT FUNCTION NORMAL & LAMDA FUNCTION GAJI BERSIH DARI LIST GAJI KOTOR]
# Gaji bersih = gaji kotor - pajak(gaji kotor * 0.1)
# gaji = [1,2,3,4,5,6,7,8,9,10,15,20]

# def gaji_bersih(yourList):
#     return yourList - yourList * 0.1
# list_gaji_bersih = list(map(gaji_bersih,gaji))
# print(list_gaji_bersih)

# #Lamda Function
# list_gaji_bersih_lambda = list(map(lambda yourList: yourList - yourList * 0.1,gaji))
# print(list_gaji_bersih_lambda)

# ===============================================================================================================
# PENGGUNAAN LOOPING DALAM LIST (List Comprehension)

# gaji = [1,2,3,4,5,6,7,8,9,10,15,20]
# list_pajak = [item * 0.1 for item in gaji]
# list_gaji_bersih = [item - item * 0.1 for item in gaji]

# print(list_pajak)
# print(list_gaji_bersih)

# PENGGUNAAN FUNCTION & LOOPING DALAM LIST (List Comprehension)
# gaji = [1,2,3,4,5,6,7,8,9,10,15,20]

# def pajak(yourList):
#     return yourList * 0.1

# # membuat variable = [eksekusi function(item), looping]
# list_pajak = [pajak(item) for item in gaji]
# print(list_pajak)

# ============================================================================================
# DATA TYPES (DICTIONARY, TUPLE, SET)

# 1. DICTIONARY(dict)
# VARIABLE = Tempat menyimpan value
# Var List = Tempat menyimpan beberapa value dan memiliki index = 0,1,2,3,4,dst
# Var String = Tempat menyimpan karakter ('...') dan memiliki index = 0,1,2,3,4,dst
# Var Dictionary = Tempat menyimpan beberapa value dan memiliki index unix/custom (bisa kita tentukan sendiri)

#DICTIONARY (dict)
# buah = {'kotak1':'mangga','key2':'nanas','kotak3':'apel','kotak4':['sawo',1000]} # id index/key bisa dicustomm(kotak1,key2,dll)

# # 1.A. GET: Mendapatkan value pada index / key tertentu
# print(buah.get('kotak1'))
# print(buah.get('kotak4'))
# # print(buah['kotak1'])
# # print(buah['key2'])
# # print(buah['kotak3'])
# # print(buah['kotak4'][0])

# identitas = {'nama':'Andi', 'usia':26, 'kewarganegaraan':'WNI', 'gaji':20000000}

# menambahkan key & value secara sementara
# data_tambahan = identitas.get('gol_darah','AB+')
# print(identitas)
# print(data_tambahan)

# # 1.B. KEYS: Menampilkan keys / nama index saja
# print(identitas.keys())

# # 1.C. VALUES: Menampilkan values data / isi dari keynya saja 
# print(identitas.values())

# # 1.D. UPDATE: Menambahkan isi dari dictionary
# new_data = {'gol_darah':'B-'}
# identitas.update(new_data)
# print(identitas)

# # 1.E. ITEM: Menampikan keseluruhan data baik keys maupun values
# print(identitas.items())
# print(list(identitas.items()))

# x = list(identitas.items())
# print(list(x[0]))

# # 1.F. POP ITEM: Menghapus item tertentu dari belakang
# identitas.popitem()
# print(identitas)

# # 1.G. POP: Menghapus item berdasarkan key tertentu
# identitas.pop('nama')
# print(identitas)

# ===================================================================================

# LATIHAN
# UBAH LIST KEDALAM DICTIONARY
# data = ['Andi', 23, 'Budi', 30, 'Dedi', 41]

# dict_data = {data[i]:data[i+1] for i in range(0, len(data),2)}
# data_baru = {data[i+1]:data[i] for i in range(0, len(data),2)}

# print(dict_data)
# print(data_baru)

# list_nama = ['Andi','Budi','Caca','Dedi','Eka']
# dict_nama = {i+1:list_nama[i] for i in range(0, len(list_nama))}

# print(dict_nama)

# =============================================================================
# LATIHAN
# Buat dictionary dengan keys (karyawan) dan values (gaji)
# karyawan = ['Ferdian', 'Giring', 'Hedi', 'Imam']
# gaji = [20, 35, 12, 17]

# dict_gaji_karyawan = {karyawan[i]:gaji[i] for i in range(0,len(karyawan))}

# # Menyisipkan / menambahkan karakter dalam tampilan dictionary
# new_dict_gaji_karyawan = {f'{i+1} {karyawan[i]}':f'Rp {gaji[i]} Juta' for i in range (0, len(karyawan))}
# print(dict_gaji_karyawan)
# print(new_dict_gaji_karyawan)

# =============================================================================================================

# 2. TUPLE = Sama seperti list tapi sudah tidak bisa diedit

# gaji = [1,2,3,4,5]
# gaji[2] = 30 # mengubah gaji index ke 2 menjadi 30
# print(gaji)

# salary = (1,2,3,4,5) # Bentuk data bertipe TUPLE
# salary[2] = 30 # perintah ini tidak bisa dijalankan di tipe data TUPLE
# print(salary)

# BAGAIMANA MENGEDIT TUPLE?
# salary = (1,2,3,4,5)
# new_salary = list(salary)
# new_salary[2] = 30
# salary = new_salary
# salary = tuple(new_salary)
# print(salary)

# ==================================================================================================

# 3. SET = Sama seperti list tapi tidak ada data double / duplicate

# Bedanya dengan list adalah semua dianggap ada
# gaji = [1, 2, 2, 3, 3, 4, 5, 5, 5]
# print(gaji)

# set tidak menampilkan data double
# salary = {1, 2, 2, 3, 3, 4, 5, 5, 5} # bentuk data bertipe SET
# # print(salary)
# # print(len(salary))

# gaji = [1, 2, 2, 3, 3, 4, 5, 5, 5,1,2,3,4,6,6,7,8,9,1,2,2,1,1,1,1,3,4,8,8,9]
# gaji_unik = set(gaji)
# print(gaji_unik)
# print(len(gaji_unik))

# =========================================================================================================
# Methods for Searching
# check1 = 5 in[1,2,3,4]
# check2 = 'wa' in "Purwadhika"
# print(check1)
# print(check2)

# =============================================================================================================
# LATIHAN
# Buat tampilan seperti ini :
# identitas = {'karyawan ke-1':['Andi', 30, 8], 'karyawan ke-2':['Budi', 40, 9], 'karyawan ke-3':['Caca',50,10]}

nama = ['Andi', 'Budi', 'Caca']
usia = [30, 40, 50]
gaji = [8, 9, 10]

identitas = {f'Karyawan ke-{i+1}':[nama[i],usia[i],gaji[i]] for i in range(0, len(nama))}
print(identitas)


# identitas2 = {'karyawan ke-1':['Andi', 30, 8], 'karyawan ke-2':['Budi', 40, 9], 'karyawan ke-3':['Caca',50,10]}

# print(identitas2)
