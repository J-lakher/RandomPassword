import random
import string

def generate_password(length):
    characters = string.ascii_letters +string.digits + string.punctuation
    password = ''.join(random.choice(characters)
for _ in range(length))
    return password

#Example usage:
Password_length = 12
generated_password = generate_password(Password_length)
print("Generated Password:", generated_password)