number = int(input())
capacity = 255
total_litters = 0

for i in range(number):
    litters = int(input())
    if litters > capacity - total_litters:
        print("Insufficient capacity!")
        continue
    total_litters += litters

print(total_litters)