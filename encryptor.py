from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import base64
import json

def load_public_key(path):
    return RSA.import_key(open(path).read())

def load_private_key(path):
    return RSA.import_key(open(path).read())

def hybrid_encrypt(msg: str, pub1_path, pub2_path):
    pub1 = load_public_key(pub1_path)
    pub2 = load_public_key(pub2_path)

    # Generate AES session key
    session_key = get_random_bytes(16)  # AES-128

    # Encrypt the message with AES-GCM
    cipher_aes = AES.new(session_key, AES.MODE_GCM)
    ciphertext, tag = cipher_aes.encrypt_and_digest(msg.encode())

    # Encrypt AES session key with both public RSA keys
    cipher_rsa_1 = PKCS1_OAEP.new(pub1)
    cipher_rsa_2 = PKCS1_OAEP.new(pub2)
    enc_session_key_1 = cipher_rsa_1.encrypt(session_key)
    enc_session_key_2 = cipher_rsa_2.encrypt(session_key)

    # Prepare JSON with base64 encoded components
    encrypted_dict = {
        'enc_session_key_1': base64.b64encode(enc_session_key_1).decode(),
        'enc_session_key_2': base64.b64encode(enc_session_key_2).decode(),
        'nonce': base64.b64encode(cipher_aes.nonce).decode(),
        'tag': base64.b64encode(tag).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode()
    }
    return json.dumps(encrypted_dict)

def hybrid_decrypt(enc_json: str, priv1_path, priv2_path):
    priv1 = load_private_key(priv1_path)
    priv2 = load_private_key(priv2_path)

    encrypted_dict = json.loads(enc_json)

    enc_session_key_1 = base64.b64decode(encrypted_dict['enc_session_key_1'])
    enc_session_key_2 = base64.b64decode(encrypted_dict['enc_session_key_2'])
    nonce = base64.b64decode(encrypted_dict['nonce'])
    tag = base64.b64decode(encrypted_dict['tag'])
    ciphertext = base64.b64decode(encrypted_dict['ciphertext'])

    cipher_rsa_1 = PKCS1_OAEP.new(priv1)
    cipher_rsa_2 = PKCS1_OAEP.new(priv2)

    # Both private keys decrypt the session key
    session_key_1 = cipher_rsa_1.decrypt(enc_session_key_1)
    session_key_2 = cipher_rsa_2.decrypt(enc_session_key_2)

    if session_key_1 != session_key_2:
        raise ValueError("Session keys mismatch!")

    # Decrypt AES encrypted message
    cipher_aes = AES.new(session_key_1, AES.MODE_GCM, nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)

    return plaintext.decode()
