import re
from logo import logo

def check_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "digit": re.search(r"\d", password) is not None,
        "special": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None,
    }

    score = sum(criteria.values())

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    print(f"\nPassword Strength: {strength}")

    if strength != "Very Strong":
        print("Suggestions:")
        if not criteria["length"]:
            print("- Password should be at least 8 characters long.")
        if not criteria["uppercase"]:
            print("- Include at least one uppercase letter.")
        if not criteria["lowercase"]:
            print("- Include at least one lowercase letter.")
        if not criteria["digit"]:
            print("- Include at least one number.")
        if not criteria["special"]:
            print("- Include at least one special character (!@#$%^&*(),.?\":{}|<>).")

    return strength == "Very Strong"
print((logo))
while True:
    password = input("Enter your password to check: ")
    if check_password_strength(password):
        print(" Great! Your password is very strong.")
        break
    else:
        print(" Please try again with a stronger password.\n")
