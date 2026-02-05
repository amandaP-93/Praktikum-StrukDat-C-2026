nilai_siswa = {
    "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
    "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
    "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

nilai_siswa["S04"] = {
    "nama": "Fafa",
    "tugas": 85,
    "uts": 80,
    "uas": 90
}

print("Nilai Akhir Siswa > 80")
for x in nilai_siswa.values():
    final = (x["tugas"] * 0.2) + (x["uts"] * 0.3) + (x["uas"] * 0.5)
    if (final > 80):
        print(f"{x["nama"]}: {final}")