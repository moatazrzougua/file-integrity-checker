
import hashlib

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


filename = input("Enter file name: ")

try:
    result = calculate_hash(filename)
    print("SHA-256:", result)

except FileNotFoundError:
    print("Error: File not found.")
