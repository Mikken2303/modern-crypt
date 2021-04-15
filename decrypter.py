from cryptography.fernet import Fernet, InvalidToken

key = input("Key: ").encode('UTF-8')
input_file = 'encrypted.txt'
output_file = 'output.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(decrypted)


except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")