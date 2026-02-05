stok = [15, 50, 30, 25, 40]

stok.append(100)
stok.insert(2, 75)
stok.sort(reverse=True)

total = 0
for x in stok:
    total += x

mean = total / len(stok)

print(mean)
print(stok)