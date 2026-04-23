# =========================
# DOUBLE LINKED LIST
# =========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # tambah kendaraan ke akhir
    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    # tampil dari depan ke belakang
    def tampilkan_maju(self):
        print("[Maju]")
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # tampil dari belakang ke depan
    def tampilkan_mundur(self):
        print("[Mundur]")
        current = self.head

        # cari node terakhir dulu
        while current and current.next:
            current = current.next

        # baru tampil mundur
        while current:
            print(current.data)
            current = current.prev

    # hapus kendaraan berdasarkan plat
    def hapus_kendaraan(self, plat):
        current = self.head

        while current:
            if current.data == plat:

                # kalau node pertama
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev

                return
            current = current.next


# =========================
# CIRCULAR LINKED LIST
# =========================

class NodeCircular:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah_petugas(self, nama):
        new_node = NodeCircular(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def giliran_berikutnya(self, n):
        current = self.head

        for i in range(n):
            print(f"Giliran {i+1}: {current.data}")
            current = current.next


# =========================
# MAIN PROGRAM (contoh run)
# =========================

if __name__ == "__main__":

    print("=== DOUBLE LINKED LIST ===")

    dll = DoubleLinkedList()
    dll.tambah_kendaraan("B 1111 AA")
    dll.tambah_kendaraan("D 2222 BB")
    dll.tambah_kendaraan("A 3333 CC")
    dll.tambah_kendaraan("B 4444 DD")

    print("Sebelum:")
    dll.tampilkan_maju()

    dll.hapus_kendaraan("A 3333 CC")

    print("Sesudah:")
    dll.tampilkan_maju()

    print()
    dll.tampilkan_mundur()

    print("\n=== CIRCULAR LINKED LIST ===")

    cll = CircularLinkedList()
    cll.tambah_petugas("Andi")
    cll.tambah_petugas("Budi")
    cll.tambah_petugas("Citra")
    cll.tambah_petugas("Dewi")

    cll.giliran_berikutnya(6)