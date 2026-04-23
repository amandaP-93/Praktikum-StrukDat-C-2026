def pisah_ganjil_genap(data_plat):
    ganjil = []
    genap = []

    for plat in data_plat:
        bagian = plat.split()      
        angka = bagian[1]          
        terakhir = int(angka[-1])  

        if terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap


data = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

ganjil, genap = pisah_ganjil_genap(data)

print("Plat Ganjil:", ganjil)
print("Plat Genap:", genap)