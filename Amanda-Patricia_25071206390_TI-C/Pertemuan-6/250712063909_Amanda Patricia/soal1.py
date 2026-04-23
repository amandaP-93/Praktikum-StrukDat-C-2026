

def registrasi_gadget(merk, tipe, harga, sn):
  

 if harga <= 1000000:
        print("error: Harga harus di atas Rp1.000.000.")
        return None 
 
 if len(sn) < 5:
        print("error: Serial Number harus minimal 5 karakter.")
        return None
 
 
 return {
        "merk": merk,
        "tipe": tipe,
        "harga": harga,
        "sn": sn,
        "status": "tersedia"
    }


inventaris = []

for i in range(3):
    print(f"\nInput Gadget ke-{i+1}")
    merk = input("Masukkan merk: ")
    tipe = input("Masukkan tipe: ")
    harga = int(input("Masukkan harga: "))
    sn = input("Masukkan Serial Number: ")
    data = registrasi_gadget(merk, tipe, harga, sn)
    if merk:
         inventaris.append(data)
    
print("\n daftar invesntaris")
for gadget in inventaris:
    print(gadget)

