times = input().split()

times = sorted(times, key=lambda x: (x[:2], x[3:5]))

print(", ".join(times))
