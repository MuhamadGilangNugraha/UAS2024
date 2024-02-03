print("==========Shimon Food==========")
Pembeli = input("Nama Pembeli : ")
print("Nama Pembeli : ")

def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n===========Menu Makanan==========")
    print("1. Nasi Uduk - Rp.4000,00") 
    print("2. Nasi Putih - Rp.3000,00") 
    print("3. Lele - Rp.10.000,00") 
    print("4. Ayam Goreng - Rp.15.000,00") 
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    porsi = int(input("Berapa Porsi : ") )
    if nomor == 1 :
        totalmakanan = porsi * 4000
        print(porsi,"Nasi Uduk = Rp.",totalmakanan)
        makan=("Nasi Uduk")
    elif nomor == 2 :
        totalmakanan = porsi * 3000
        print(porsi,"Nasi Putih = Rp.",totalmakanan)
        makan=("Nasi Putih")
    elif nomor == 3 :
        totalmakanan = porsi * 10000
        print(porsi,"Lele = Rp.",totalmakanan)
        makan=("Lele")
    elif nomor == 4 :
        totalmakanan = porsi * 15000
        print(porsi,"Ayam Goreng = Rp.",totalmakanan)
        makan=("Ayam Goreng")
    else :
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!! ")
        makanan()

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n===========Menu Minuman==========")
    print("1. Air Putih - Rp.1000,00") 
    print("2. Es Teh Manis - Rp.3000,00") 
    print("3. Lemon Tea - Rp.5.000,00") 
    print("4. Mangga Juice - Rp.15.000,00") 
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    gelas = int(input("Berapa gelas : ")) 
    if nomor == 1 :
        totalminuman = porsi * 1000
        print(gelas,"Air Putih = Rp.",totalminuman)
        minum=("Air Putih")
    elif nomor == 2 :
        totalminuman = porsi * 3000
        print(gelas,"Es Teh Manis = Rp.",totalminuman)
        minum=("Es Teh Manis")
    elif nomor == 3 :
        totalminuman = porsi * 5000
        print(gelas,"Lemon Tea = Rp.",totalminuman)
        minum=("Lemon Tea")
    elif nomor == 4 :
        totalminuman = porsi * 15000
        print(gelas,"Mangga Juice = Rp.",totalminuman)
        minum=("Mangga Juice")
    else :
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!! ")
        minuman()

makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\nTotal yang harus dibayar : ",total_semua)
uang = int(input("Uang Tunai Pembeli : Rp. "))
kembalian = int(uang - total_semua)
print("Kembalian :", kembalian)

print("\n==========S T R U K B E L I=========")
print("Nama\t\t:",Pembeli)
print("Beli\t\t:",porsi,makan,"(Rp.",totalmakanan,")")
print("Beli\t\t:",gelas,minum,"(Rp.",totalminuman,")")
print("Tagihan\t\t:Rp.",total_semua)
print("Dibayar\t\t:Rp.",uang)
print("Kembalian\t:Rp.",kembalian)

print("==========Terimakasih Telah==========")
print("=============Berkunjung=============")
