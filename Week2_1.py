# LOOPING
# Algoritma Pengulangan
# Supaya code kita lebih efisien dalam menjalankan perintah yg berulang

# JENIS LOOPING:
# 1. WHILE LOOP
# 2. FOR LOOP

# 1. WHILE LOOP
# angka = 1 # angka awal adalah 1
# while angka <= 6: # Selama angka kurang dari 6, maka jalankan perintah dibawa
#     print("Hallo") # tampilkan Hallo
#     angka += 1

# 2. FOR LOOP
# BELAJAR MEMBUAT LIST DATA
# contoh_list = [1, 2, 3, 4, 5]
# conttoh_list2 = ['a', 'b', 'c', 4, 5]
# print(contoh_list)
# print(conttoh_list2)

# list_item = list(range(1,11,2))# Membuat list dengan range 1 sampai 11, dengan step 2
# print(list_item)

#BELAJAR MENGGUNAKAN FOR LOOP
# list_item = list(range(1,11,2))# Membuat list dengan range 1 sampai 11, dengan step 2
# print(list_item)

# for item in range(1,11,2):
#     print(item)# Ini untuk menampilkan itemnya saja tanpa tampilan list yg pake [1,2,dst..]

# for item in range(0,5):# pengulangan 0 sampai 5 : 0, 1, 2, 3, 4
#     print('Hallo')

# for i in range(10):
#     print(f'Nomor urut {i+1}')

# for i in range(0,21,2):
#     print(f'Nomor urut {i}')

# LOOP DRAWING
# teks = '' # membuat string kosong
# teks += 'Halo' # menambah value baru ke variable teks yg masih kosong
# print(teks) # tampilkan variable teks

# teks = ''
# for i in range(0,5):
#     teks += ' * ' # untuk variable harus masuk ke indentation (tab 1 kali)
#     print(teks) # menampilkan * di dlm indentation
# print(teks) # menampilkan * diluar indentation

# teks2 = ''
# for i in range()

# LATIHAN
# Buat tampilan seperti ini :
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# teks = ''
# for i in range(0,5): # pengulangan sebanyak jumlah item di range 0 - 5 # Perintah looping awal
#     for i in range(0,5): # pengulangan ke 2 perintah sebanyak jumlah item di range 0 - 5 # Perintah looping akhir
#         teks +=(' * ') # Perintah A
#     teks += '\n'       # Perintah B
# print(teks) 

#LATIHAN
# Buat tampilan seperti ini :
# * 
# * *
# * * * 
# * * * * *

# teks = ''
# for x in range(0,5):
#     for y in range(0,x+1): 
#         teks +=(' * ')
#     teks += '\n'
# print(teks) 

