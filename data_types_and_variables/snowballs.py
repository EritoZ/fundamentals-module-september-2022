snowballs = int(input())
best_snowball = 0
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0

for snowball in range(snowballs):
    snowball_weight = int(input())
    time_to_target = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / time_to_target) ** snowball_quality

    if snowball_value > best_snowball:
        best_snowball = snowball_value
        best_snowball_weight = snowball_weight
        best_snowball_time = time_to_target
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {int(best_snowball)} ({best_snowball_quality})")