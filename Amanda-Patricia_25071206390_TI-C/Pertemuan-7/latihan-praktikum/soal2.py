class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambahKendaraan(self, plat):
        nodeBaru = Node(plat)

        if self.head is None:
            self.head = nodeBaru
        else:
            sekarang = self.head
            while sekarang.next:
                sekarang = sekarang.next
            sekarang.next = nodeBaru

    def hapusKendaraan(self, plat):
        sekarang = self.head
        sebelumnya = None

        while sekarang:
            if sekarang.plat == plat:
                if sebelumnya is None:
                    self.head = sekarang.next
                else:
                    sebelumnya.next = sekarang.next
                return
            sebelumnya = sekarang
            sekarang = sekarang.next

    def tampilkan(self):
        sekarang = self.head
        while sekarang:
            print(sekarang.plat, end=" -> ")
            sekarang = sekarang.next
        print("None")


parkir = LinkedList()

parkir.tambahKendaraan("B 1234 ABC")
parkir.tambahKendaraan("D 8888 XYZ")
parkir.tambahKendaraan("A 111 TUV")
parkir.tambahKendaraan("B 2022 EFG")

print("Antrean kendaraan:")
parkir.tampilkan()

parkir.hapusKendaraan("D 8888 XYZ")

print("Setelah kendaraan mogok dihapus:")
parkir.tampilkan()