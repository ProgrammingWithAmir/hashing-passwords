"""
    Hashing Passwords Using Python
"""
# importing modules
import hashlib

# password input
password = str(input('Enter Your Password: '))

# hashing given password
hashtype = 'sha256' # It can be other hashtypes like md5, sha512 ...
m = getattr(hashlib, hashtype)()
m.update(password.encode())

# output
print('hash-type: ' + hashtype)
print(m.hexdigest())