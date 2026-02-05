barang = ("B001", "Laptop Gaming", 15000000)

print(barang[2])

# Kode:
# barang[2] = 14000000

# Penjelasan:
# Kode ini akan mengalami error karena Tuple bersifat immutable (tidak bisa diubah).
# Oleh karena itu, Tuple harus dikonversi menjadi List terlebih dahulu.

kode, nama, harga = barang
