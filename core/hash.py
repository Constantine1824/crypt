import uuid
import hashlib

def hash_password(password):
    salt = uuid.uuid64().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    