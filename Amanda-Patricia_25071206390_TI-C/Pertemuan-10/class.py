# Menggunakan Class
print("Class")

class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


s = StackList()
s.push("formula1.com")
s.push("motogp.com")
s.push("redbull.com")

print(s.peek())
print(s.pop())
print(s.size())
print(s.is_empty())


