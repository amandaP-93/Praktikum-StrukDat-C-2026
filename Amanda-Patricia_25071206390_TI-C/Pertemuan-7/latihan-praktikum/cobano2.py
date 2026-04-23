class Node:
  def __init__(self, plat):
    self.plat = plat
    self.next = None


def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.plat, end=" -> ")
    currentNode = currentNode.next
  print("null")


def hapusKendaraan(head, plat):
  current = head
  prev = None

  while current:
    if current.plat == plat:
      if prev is None:
        head = current.next
      else:
        prev.next = current.next
      return head
    prev = current
    current = current.next

  return head


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

print("Antrean awal:")
traverseAndPrint(node1)

node1 = hapusKendaraan(node1, "A 111 TUV")

print("Setelah kendaraan mogok dihapus:")
traverseAndPrint(node1)