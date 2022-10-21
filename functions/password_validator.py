def password_validate(password):
    number_counter = 0
    validation = []
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        validation.append("Password must be between 6 and 10 characters")
        is_valid = False
    for i in password:
        if not 48 <= ord(i) <= 58 and not 65 <= ord(i) <= 90 and not 97 <= ord(i) <= 122:
            validation.append("Password must consist only of letters and digits")
            is_valid = False
            break
    for i in password:
        if 48 <= ord(i) <= 57:
            number_counter += 1
    if number_counter < 2:
        validation.append("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        validation.append("Password is valid")

    return "\n".join(validation)


password = input()

print(password_validate(password))
