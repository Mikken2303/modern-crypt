from cryptography.fernet import Fernet

key = input("Key: ").encode('UTF-8')

input_file = 'test.txt'
output_file = 'encrypted.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

