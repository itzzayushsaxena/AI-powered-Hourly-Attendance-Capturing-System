import base64
from cryptography.fernet import Fernet

variable = str(4).encode()
print(variable)

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(variable)
print(token)
ans = f.decrypt(token)
print(ans)
print(ans.decode("utf-8"))