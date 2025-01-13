import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    """
    Generate a random password based on the selected character types and length.
    """
    # Define character sets
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    lowercase_chars = string.ascii_lowercase if use_lowercase else ""
    number_chars = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special_chars else ""

    # Combine selected character sets
    all_chars = uppercase_chars + lowercase_chars + number_chars + special_chars
    if not all_chars:
        print("Error: At least one character type must be selected. Please try again.")
        return None

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    """
    Main function to interact with the user and generate a password.
    """
    print("Welcome to the Password Generator!")
    
    # Input settings
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input for password length. Please enter a valid number.")
        return

    # Character type selection
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == "y"

    # Generate password
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

    # Display the result
    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
