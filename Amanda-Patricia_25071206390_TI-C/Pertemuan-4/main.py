from tabulate import tabulate
from kurs import kurs
from konverter import idr_ke_mata_uang, mata_uang_ke_idr

print("=== KONVERTER MATA UANG ===")

# tampilkan tabel kurs
data = []
for kode, nilai in kurs.items():
    data.append([kode, f"{nilai:,}".replace(",", ".")])

print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

if dari == "IDR":
    hasil = idr_ke_mata_uang(jumlah, ke)
    print(f"Rp {jumlah:,.0f} = {hasil:.2f} {ke}")

elif ke == "IDR":
    hasil = mata_uang_ke_idr(jumlah, dari)
    print(f"{jumlah} {dari} = Rp {hasil:,.0f}")

else:
    print("Konversi hanya mendukung IDR ke mata uang lain atau sebaliknya.")
    