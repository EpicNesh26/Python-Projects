import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    special = string.punctuation if include_special else ''
    
    # Combine character sets
    all_characters = lowercase + uppercase + numbers + special
    
    if not all_characters:
        raise ValueError("No character sets selected. Please select at least one character set.")
    
    # Ensure the password contains at least one character from each selected set
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_special:
        password.append(random.choice(special))
    
    # Fill the rest of the password length with random choices from the combined set
    while len(password) < length:
        password.append(random.choice(all_characters))
    
    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
            return
        
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
