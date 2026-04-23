class Node:
  def __init__(self, plat):
    self.plat = plat
    self.next = None


def tampilkan_antrean(head):
  currentNode = head
  while currentNode:
    print(currentNode.plat, end=" -> ")
    currentNode = currentNode.next
  print("null")


def sisipkan_vip(head, plat_baru, plat_target):
  current = head

  while current:
    if current.plat == plat_target:
      nodeBaru = Node(plat_baru)
      nodeBaru.next = current.next
      current.next = nodeBaru
      return head
    current = current.next

  return head


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")

node1.next = node2
node2.next = node3


print("Antrean awal:")
tampilkan_antrean(node1)


node1 = sisipkan_vip(node1, "VIP 9999", "D 8888 XYZ")

print("Setelah VIP disisipkan:")
tampilkan_antrean(node1)  