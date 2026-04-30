class Node:
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node ('A')
        self.root.kiri = Node ('B')
        self.root.kanan = Node ('C')
        self.root.kiri.kiri = Node ('D')
        self.root.kiri.kanan = Node ('E')
        self.root.kanan.kanan = Node ('F')

    def traverse_preorder(self,node, hasil):
        if node:
            hasil.append(node.data)
            self.traverse_preorder (node.kiri, hasil)
            self.traverse_preorder (node.kanan, hasil)
        return " - ".join(hasil)
    
    def traverse_inorder(self,node, hasil):
        if node:
            self.traverse_inorder (node.kiri, hasil)
            hasil.append(node.data)
            self.traverse_inorder (node.kanan, hasil)
        return " - ".join(hasil)

    def traverse_postorder(self,node, hasil):
        if node:
            self.traverse_postorder (node.kiri, hasil)
            self.traverse_postorder (node.kanan, hasil)
            hasil.append(node.data)
        return " - ".join(hasil)

    def get_leaf_nodes(self, node, leaf):
        if node:
            if not node.kiri and not node.kanan:
                leaf.append(node.data)
            self.get_leaf_nodes(node.kiri, leaf)
            self.get_leaf_nodes(node.kanan, leaf)
        return ", ".join(leaf)


tree = BinaryTree()
tree.insert_manual()

print ('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print ('====================================== ')
print ('[INFO] Membangun Struktur Gudang...')
print ('[INFO] Struktur berhasil dibuat.')

print ('\nHASIL AUDIT')
print(f"1. Pre-Order  : {tree.traverse_preorder(tree.root, [])}")   
print(f"2. In-Order   : {tree.traverse_inorder(tree.root, [])}")   
print(f"3. Post-Order : {tree.traverse_postorder(tree.root, [])}")
    
print(f"\n[DATA] Gudang Ujung (Leaf Nodes): {tree.get_leaf_nodes(tree.root, [])}")
print("======================================")
print("Audit Selesai!")