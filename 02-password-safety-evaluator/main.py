while True:

    password = input("Enter the password: ").strip()
    if password.strip() == "" :
        print("ask again, no crash")
        continue

    has_length = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    if len(password) >=8:
        has_length = True

    for ch in password:
        if ch.isupper():
            has_upper = True

        if ch.islower():
            has_lower = True

        if ch.isdigit():
            has_digit = True

        if not ch.isalnum() and not ch.isspace():
            has_symbol = True

    score = 0

    if has_length:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_symbol:
        score += 1

    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"

    print(f"'{password}' → {score}/5 {strength}")

    if not has_length:
        print("Use at least 8 characters.")

    if not has_upper:
        print("Add an uppercase letter.")

    if not has_lower:
        print("Add a lowercase letter.")

    if not has_digit:
        print("Add a number.")

    if not has_symbol:
        print("Add a special character.")

    choice = input("Check another password? (yes/no): ")

    if choice == "no":
        break


