# Menggunakan Linked List
print("\nLinked List")

class Node:
    def __init__(self, url):
        self.url = url
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top == None

    def push(self, url):
        baru = Node(url)
        baru.next = self.top
        self.top = baru
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        ambil = self.top.url
        self.top = self.top.next
        self.count -= 1
        return ambil

    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count


s2 = StackLinkedList()
s2.push("redbull.com")
s2.push("formula1.com")
s2.push("motogp.com")

print(s2.peek())
print(s2.pop())
print(s2.size())
print(s2.is_empty())


