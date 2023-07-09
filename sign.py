import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

def generate_rsa_signature(data, private_key_path, signature_path):
    # データのハッシュ値を計算
    hash_value = hashlib.sha256(data).digest()

    # 秘密鍵の読み込み
    with open(private_key_path, 'r') as f:
        private_key = RSA.import_key(f.read())

    # データの署名
    signer = PKCS1_v1_5.new(private_key)
    signature = signer.sign(SHA256.new(hash_value))

    # 署名をファイルに出力
    with open(signature_path, 'wb') as file:
        file.write(signature)

    print("RSA Signature generated and saved to", signature_path)

# 署名を生成するテキストファイルと秘密鍵のパスを指定
file_path = "input.txt"
private_key_path = "private.pem"
signature_path = "signature.bin"

# テキストファイルを読み込む
with open(file_path, 'rb') as file:
    data_to_sign = file.read()

# RSA署名を生成してファイルに出力
generate_rsa_signature(data_to_sign, private_key_path, signature_path)
