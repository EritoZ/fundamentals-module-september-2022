lines = int(input())
positives = []
negatives = []
for i in range(lines):
    n = int(input())
    if n >= 0:
        positives.append(n)
    else:
        negatives.append(n)

print(f"""{positives}
{negatives}
Count of positives: {len(positives)}
Sum of negatives: {sum(negatives)}""")
