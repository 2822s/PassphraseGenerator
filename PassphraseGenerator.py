import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
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

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
