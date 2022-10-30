class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")

    def __repr__(self):
        return self.sender


emails = []
command = input()
while command != "Stop":
    info = command.split()
    sender, receiver, content = info
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()

sent_or_not = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    email.get_info()
