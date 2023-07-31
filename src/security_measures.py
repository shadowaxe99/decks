```python
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Load the secret key from environment variable
SECRET_KEY = os.getenv('SECRET_KEY')

# Create a Fernet object
cipher_suite = Fernet(SECRET_KEY)

def encrypt_data(data):
    """
    Function to encrypt data using Fernet symmetric encryption
    """
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

def decrypt_data(cipher_text):
    """
    Function to decrypt data using Fernet symmetric encryption
    """
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text.decode()

def implementSecurity(data):
    """
    Function to implement security measures
    """
    encrypted_data = encrypt_data(data)
    return encrypted_data
```