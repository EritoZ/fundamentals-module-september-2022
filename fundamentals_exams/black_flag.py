days = int(input())
plundering = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, days + 1):
    total_plunder += plundering

    if day % 3 == 0:
        total_plunder += plundering * 0.5

    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder / expected_plunder * 100:.2f}% of the plunder.")
