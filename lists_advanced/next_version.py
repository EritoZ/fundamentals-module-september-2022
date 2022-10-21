version = int("".join(input().split(".")))

new_version = ".".join([n for n in str(version + 1)])

print(new_version)
