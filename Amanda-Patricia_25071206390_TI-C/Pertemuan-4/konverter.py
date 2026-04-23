from kurs import kurs

def idr_ke_mata_uang(jumlah, kode):
    return jumlah / kurs[kode]

def mata_uang_ke_idr(jumlah, kode):
    return jumlah * kurs[kode]