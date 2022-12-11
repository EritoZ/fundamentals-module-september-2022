log_dict = {}
n_logs = int(input())

for log in range(n_logs):
    ip, name, duration = input().split()

    if name not in log_dict:
        log_dict[name] = [0, []]

    log_dict[name][0] += int(duration)

    if ip not in log_dict[name][1]:
        log_dict[name][1].append(ip)

log_dict = dict(sorted(log_dict.items()))

for user in log_dict:
    log_dict[user][1] = sorted(log_dict[user][1])

    print(f"{user}: {log_dict[user][0]} [{', '.join(log_dict[user][1])}]")
