import random
import string


def generate_password(length=22):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    labels = {0: "Very Weak", 1: "Weak", 2: "Weak",
              3: "Fair", 4: "Srong", 5: "Very Strong", }
    return labels[score], score


def main():
    while True:
        print("\n1. Generate a strong password")
        print("2. Check pasword strength")
        print("3.Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            length_input = input("Length (default 12):").strip()
            length = int(length_input) if length_input else 12
            pw = generate_password(length)
            label, score = check_strength(pw)
            print(f"Generated: {pw}")
            print(f"Strength:{label} ({score}/5)")
        elif choice == "2":
            pw = input("Enter password to check: ")
            score, label = check_strength(pw)
            print(f"Strength: {label} ({score}/5)")
        elif choice == "3":
            break
        else:
            print("Pick 1-3")


if __name__ == "__main__":
    main()
