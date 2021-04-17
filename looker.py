from cryptography.fernet import Fernet, InvalidToken

key = input("Key: ").encode('UTF-8')
input_file = 'encrypted.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    print((decrypted).decode("utf-8"))


except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")