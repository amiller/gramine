import os
import random
import string
import hashlib

def generate_fake_users(num_users=1000, output_file="/output/output.dat"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "wb") as f:
        for _ in range(num_users):
            username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            email = f"{username}@example.com"
            password = ''.join(random.choices(string.digits + string.ascii_letters, k=12))
            user_data = f"{username},{email},{password}\n".encode().ljust(4096, b" ")
            f.write(user_data)

def print_random_entry_hash(output_file="/output/output.dat"):
    with open(output_file, "rb") as f:
        random_entry_offset = random.randint(0, os.path.getsize(output_file) - 4096)
        f.seek(random_entry_offset)
        random_entry = f.read(4096).rstrip(b" ")
        print(f"Random entry: {random_entry.decode()}")
        print(f"SHA256 hash: {hashlib.sha256(random_entry).hexdigest()}")

if __name__ == "__main__":
    generate_fake_users()
    print_random_entry_hash()
