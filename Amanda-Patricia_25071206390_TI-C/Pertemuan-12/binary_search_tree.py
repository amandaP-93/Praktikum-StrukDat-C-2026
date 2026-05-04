class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # tambah data
    def insert(self, id_buku, judul):
        node_baru = Node(id_buku, judul)
        if self.root is None:
            self.root = node_baru
        else:
            self._insert(self.root, node_baru)

    def _insert(self, current, node_baru):
        if node_baru.id < current.id:
            if current.left is None:
                current.left = node_baru
            else:
                self._insert(current.left, node_baru)
        else:
            if current.right is None:
                current.right = node_baru
            else:
                self._insert(current.right, node_baru)

    # cari data
    def search(self, id_buku):
        return self._search(self.root, id_buku)

    def _search(self, current, id_buku):
        if current is None:
            return None
        if id_buku == current.id:
            return current
        elif id_buku < current.id:
            return self._search(current.left, id_buku)
        else:
            return self._search(current.right, id_buku)

    # tampil urut
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.id, "-", node.judul)
            self.inorder(node.right)

    # nilai terkecil
    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.id

    # nilai terbesar
    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.id

    # tinggi tree
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))


# ===== program utama =====
bst = BST()

# input data buku
bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

# tampil urut
print("Data buku (urut):")
bst.inorder(bst.root)

# pencarian
print("\nCari ID 60:", "Ada" if bst.search(60) else "Tidak ada")
print("Cari ID 100:", "Ada" if bst.search(100) else "Tidak ada")

# min dan max
print("\nID terkecil:", bst.get_min())
print("ID terbesar:", bst.get_max())

# tinggi tree
print("\nTinggi tree:", bst.height(bst.root))