import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars, avoid_similar):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    if avoid_similar:
        similar_chars = 'l1O0'
        lowercase = ''.join(c for c in lowercase if c not in similar_chars)
        uppercase = ''.join(c for c in uppercase if c not in similar_chars)
        numbers = ''.join(c for c in numbers if c not in similar_chars)

    all_characters = lowercase + uppercase + numbers + special_chars
    password = []
    
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special_chars:
        password.append(random.choice(special_chars))
    
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    
    return ''.join(password)

def password_strength(length, use_uppercase, use_numbers, use_special_chars):
    strength = "Weak"
    if length >= 12 and (use_uppercase or use_numbers or use_special_chars):
        strength = "Strong"
    elif length >= 8:
        strength = "Medium"
    return strength

def main():
    print("Welcome to the Random Password Generator!")
    
    min_length = 8
    max_length = 20
    length = int(input(f"Enter the desired password length ({min_length}-{max_length}): "))
    length = max(min_length, min(length, max_length))
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    avoid_similar = input("Avoid similar characters (l, 1, O, 0)? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars, avoid_similar)
    strength = password_strength(length, use_uppercase, use_numbers, use_special_chars)
    
    print(f"Your generated password is: {password}")
    print(f"Password strength: {strength}")
    
    save_to_file = input("Do you want to save the password to a file? (y/n): ").lower() == 'y'
    if save_to_file:
        with open("generated_password.txt", "w") as f:
            f.write(password)
        print("Password saved to generated_password.txt")

if __name__ == "__main__":
    main()

