import re

n_emails = int(input())
email_dict = {}
valid_email_pattern = r"([A-Za-z]{5,})@([a-z]{3,}(?:\.com|\.bg|\.org))$"

for _ in range(n_emails):
    email = input()

    valid_email = re.search(valid_email_pattern, email)
    if valid_email is not None:
        username = valid_email.group(1)
        domain = valid_email.group(2)

        if domain not in email_dict:
            email_dict[domain] = []

        if username not in email_dict[domain]:
            email_dict[domain].append(username)

email_dict = dict(sorted(email_dict.items(), key=lambda domain: len(domain[1]), reverse=True))

for domain in email_dict:
    print(f"{domain}:")
    for user in email_dict[domain]:
        print(f"### {user}")
