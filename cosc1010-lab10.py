# Quinn Kwiatkowski
# UWYO COSC 1010
# Submission Date: 11/24/2024
# Lab 10
# Lab Section: 14
# Sources, people worked with, help given to: None

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use"""
    # ^ YIPIEEE
    # Converts string to 'utf-8'. Hashes with 'sha256' returns the final value in uppercase
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

def crack_password(hash_file_path, passord_list_path):
    try:
        # Open the 'hash' file in read mode
        with open(hash_file_path, 'r') as hash_file:
            # Read the contents and strip any whitespace around the password
            target_hash = hash_file.read().strip() 
    except FileNotFoundError:
        # Missing file error
        print(f'Error: hash file was not found, wompity womp')
        return # Exits the program
    except IOError:
        # Permissions error
        print(f'Error: unable to read that john')
        return # Exits the program
    
    try:
        # Open the 'rockyou.txt.' file in read mode, ignoring characers that it can not decode
        with open(passord_list_path, 'r', encoding='utf-8', errors='ignore') as password_file:
            # Iterates over each line in the file
            for line in password_file:
                # Strip any white space in the password
                password = line.strip()
                # Compares hash of the current password with the target hasg
                if get_hash(password) == target_hash:
                    # If found print the matching password
                    print(f'Password found: {password}')
                    return # Exits the program
    except FileNotFoundError:
        # Missing file error
        print(f'Error: hash file was not found, wompity womp')
        return # Exits the program
    except IOError:
        # Permissions error
        print(f'Error: unable to read that john')
        return # Exits the program
    else: 
        print("Password not found in the forbes 100 list.")
    
# Runing the function
hash_file_path = 'hash' # Specifies specific path to the 'hash'
password_list_path = 'rockyou.txt' # Specifies specific path the 'rockyou.txt'

crack_password(hash_file_path, password_list_path) 

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
