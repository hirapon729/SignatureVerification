import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

# RSAキーペアの作成
key_pair = RSA.generate(2048)
private_key = key_pair.export_key()
private_key_file = open("private.pem","wb")
private_key_file.write(private_key)
private_key_file.close()

public_key = key_pair.public_key().export_key()
public_key_file = open("public.pem","wb")
public_key_file.write(public_key)
public_key_file.close()

print("RSA Key Pair is Generated")

