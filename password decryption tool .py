import hashlib

# Function to hash a string using various algorithms
def hash_string(string, algorithm):
    if algorithm == "md5":
        return hashlib.md5(string.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(string.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(string.encode()).hexdigest()
    else:
        return None

# Function to brute force a hash
def brute_force_crack(target_hash, algorithm, charset, max_length):
    from itertools import product

    for length in range(1, max_length + 1):
        for combination in product(charset, repeat=length):
            guess = ''.join(combination)
            hashed_guess = hash_string(guess, algorithm)
            if hashed_guess == target_hash:
                return guess

    return None

# Example usage
if __name__ == "__main__":
    target_hash = "d41d8cd98f00b204e9800998ecf8427e"  # Replace with your target hash
    algorithm = "md5"  # You can change this to "sha1" or "sha256" if needed
    charset = "abcdefghijklmnopqrstuvwxyz0123456789"  # Character set for brute force
    max_length = 4  # Maximum length of the brute force string

    cracked_password = brute_force_crack(target_hash, algorithm, charset, max_length)

    if cracked_password:
        print(f"Hash successfully cracked! The original string is: {cracked_password}")
    else:
        print("Hash not cracked. Try increasing the length or using a different character set.")

Explanation:
'''
    The hash_string function hashes a given string using various hash algorithms (MD5, SHA-1, or SHA-256).

    The brute_force_crack function attempts to crack a target hash using brute force. It generates all possible combinations of characters from the specified character set up to a given maximum length and checks if their hash matches the target hash.

    In the example usage, replace target_hash with the hash you want to crack, choose the hash algorithm, character set, and maximum length for the brute force search.'''

