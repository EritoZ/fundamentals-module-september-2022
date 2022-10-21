integers = sorted(list(map(int, input().split(" "))), reverse=True)
greater_than = False
biggest = []
counter = 0
average_value = sum(integers) / len(integers)

for i in range(len(integers)):
    counter += 1
    if integers[i] > average_value:
        greater_than = True
        biggest.append(integers[i])
    if counter == 5:
        break

if not greater_than:
    print("No")
else:
    print(" ".join(list(map(str, biggest))))
