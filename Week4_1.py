# CLASS (Object Oriented Programming/OOP)

# Class = Cetakan

# Contoh 'Cetakan Hewan'
# class hewan:

#     # class attreibute:
#     spesies = 'kambing'

#     # instance attribute
#     def __init__(self, asal, bobot, usia):
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia

# # mengisi class hewan
# gaga = hewan('Garut',40, 8)
# tutul = hewan('Tulungagung',47, 7)

# mengakses 'class attribute'
# print(f'Gaga adalah seekor {gaga.__class__.spesies}')

# print('Gaga adalah seekor {g.spesies}. Tutul juga seekor {t.spesies}. Gaga berasal dari {g.asal}. Sedangkan Tutul berasal dari {t.asal}.'.format(g=gaga, t=tutul))
# print('Tahun ini, Tutul menginjak usia {t.usia} tahun. Lebih muda setahun daru usia Gaga ({g.usia})'.format(g=gaga, t=tutul))
# print('Meskipin lebih muda, Tutul memiliki bobot lebih tinggi ({t.bobot} kg) daripada Gaga ({g.bobot})'.format(g=gaga, t=tutul))

#==============================================================================================================================
# METHOD = function in class

# class hewan:

#     # class attreibute:
#     spesies = 'kambing'

#     # instance attribute
#     def __init__(self, nama, asal, bobot, usia):
#         self.nama = nama
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia
    
#     # instance methods / function
#     def makan(self, makanan):
#         return f'{self.nama} sedang menikmati {makanan}.'

#     def sate(self):
#         tusuk_sate = self.bobot * 20
#         return f'{self.nama} bisa diolah menjadi {tusuk_sate} tusuk sate'

# # mengisi cetakan 'class'
# kambing_baru = hewan('Etawa', 'Garut', 45, 9)

# # uji coba methods
# print(kambing_baru.makan('Daun Pusang'))
# print(kambing_baru.sate())

# =============================================================================================================
# LATIHAN MEMBUAT CLASS CALCULATOR
# class calculator:
#     def tambah(self, x, y):
#         return x + y
#     def kurang(self, x, y):
#         return x - y
#     def kali(self, x, y):
#         return x * y
#     def bagi(self, x, y):
#         return x / y
#     def pangkat(self, x, y):
#         return x ** y

# print(calculator().tambah(4,5))
# print(calculator().kurang(40,5))
# print(calculator().kali(2,7))
# print(calculator().bagi(40,5))
# print(calculator().pangkat(4,3))

# ========================================================================================================================
# LATIHAN BUAT CALCULATOR STATISTIK
# Buatlah class yang berisi method dengan fitur:
# 1. Menghitung nilai minimun dalam list (tidak boleh pake built in function)
# 2. Menghitung nulai maksimum dalam list (tidak boleh pake built in function)
# 3. Menghitung panjang anggota dalam list (tidak boleh pakai built in function)
# 4. Menghitung mean (tidak boleh pakai built in function)
# 5. Menghitung standard deviasi 

data = [2, 3, 4, 5, 6, 7, 8, 8, 9, 21, 3, 2, 5, 4, 1, 5, 12]

class statistik:
    def minimum(self, yourlist):
        min = yourlist[0]
        for i in yourlist:
            if i < min:
                min = i
        return min
    
    def maximum(self, yourlist):
        maks = yourlist[0]
        for i in yourlist:
            if i > maks:
                maks = i
        return maks
    
    def panjanglist(self, yourlist):
        hitung = 0
        for i in yourlist:
            hitung = hitung + 1
        return hitung

    def mean(self, yourlist):
        jml = 0
        lis = 0
        rt2 = 0
        for i in yourlist:
            lis = lis + 1
            jml += i
            rt2 = jml / lis
        return rt2

    def deviasi(self, yourlist):
        n = 0
        jml = 0
        rt2 = 0
        dev = 0
        for i in yourlist:
            n = n + 1
            jml += i
            rt2 = jml / n
            dev += (i - rt2)**2
        return (dev/n)**0.5

    def deviasi2(self, yourlist):
        n = 0
        jml = 0
        rt2 = 0
        for i in yourlist:
            n = n + 1
            jml += i
            rt2 = jml / n
        
        total = 0
        for i in yourlist:
            total += (i - rt2)**2

        return (total/n)**0.5



print(statistik().minimum(data))   
print(statistik().maximum(data)) 
print(statistik().panjanglist(data)) 
print(statistik().mean(data)) 
print(statistik().deviasi2(data)) 
print(statistik().deviasi(data)) 