from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def load_public_key(path):
    return PKCS1_OAEP.new(RSA.import_key(open(path).read()))

def load_private_key(path):
    return PKCS1_OAEP.new(RSA.import_key(open(path).read()))

def encrypt_message(msg: str, pub1_path, pub2_path):
    pub1 = load_public_key(pub1_path)
    pub2 = load_public_key(pub2_path)
    enc1 = pub2.encrypt(msg.encode())
    enc2 = pub1.encrypt(enc1)
    return base64.b64encode(enc2).decode()

def decrypt_message(cipher_b64: str, priv1_path, priv2_path):
    priv1 = load_private_key(priv1_path)
    priv2 = load_private_key(priv2_path)
    raw = base64.b64decode(cipher_b64)
    dec1 = priv1.decrypt(raw)
    dec2 = priv2.decrypt(dec1)
    return dec2.decode()