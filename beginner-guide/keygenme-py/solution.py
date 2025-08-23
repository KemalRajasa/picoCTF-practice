import hashlib
from cryptography.fernet import Fernet
import base64
bUsername_trial = b"ANDERSON"
hash_user = hashlib.sha256(bUsername_trial).hexdigest()
flag = hash_user[4] + hash_user[5] + hash_user[3] + hash_user[6] + hash_user[2] + hash_user[7] + hash_user[1] + hash_user[8]
print(flag)
