#source: https://youtube.com/shorts/wdG37kGJyCY?si=GOad8xKrd6d5GlRT

import os

def generate_key(lenght):
  return os.urandom(lenght)

def xor(data, key):
  return bytes([data[i] ^ key[i] for i in range(len(data))])

def encrypt(message, key):
  if len(message) != len(key):
    raise ValueError("Key lenght should equal message len")
  return xor(message, key)

def decrypt(ciphertext, key):
  if len(ciphertext) != len(key):
    raise ValueError("Key lenght should equal message len")
  return xor(ciphertext, key)

def main():
  message = b"When you reach for the stars, you are reaching for the farthest thing out there. When you reach deep into yourself, it is the same thing, but in the opposite direction. If you reach in both directions, you will have spanned the universe."
  
  key = generate_key(len(message))

  ciphertext = encrypt(message, key)
  print(f"Encrypted test: {ciphertext}")

  decrypted_message = decrypt(ciphertext, key)
  print(f"Decrypted message: {decrypted_message.decode()}")

if __name__ == "__main__":
  main()
