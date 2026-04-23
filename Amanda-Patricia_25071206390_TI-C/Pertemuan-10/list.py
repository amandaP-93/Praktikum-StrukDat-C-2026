# Menggunakan List
print("\nList")

stack = []

def is_empty():
    return len(stack) == 0

def push(url):
    stack.append(url)

def pop():
    if is_empty():
        return "Riwayat kosong"
    return stack.pop()

def peek():
    if is_empty():
        return None
    return stack[-1]

def size():
    return len(stack)


push("motogp.com")
push("redbull.com")
push("formula1.com")

print(peek())
print(pop())
print(size())
print(is_empty())