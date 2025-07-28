from note_manager import hybrid_decrypt,hybrid_encrypt
msg = "I love you"
enc = hybrid_encrypt(msg, "keys/Fpublic.pem", "keys/Lpublic.pem")
dec = hybrid_decrypt(enc, "keys/Fprivate.pem", "keys/Lprivate.pem")
print(dec)