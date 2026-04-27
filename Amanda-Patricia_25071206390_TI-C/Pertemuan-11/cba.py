class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong!")
            return
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed.nama} (keluhan: {removed.keluhan})")

    def peek(self):
        if self.is_empty():
            print("Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama} — {self.head.keluhan}")

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        
        current = self.head
        i = 1
        print("[ANTRIAN SAAT INI]") 