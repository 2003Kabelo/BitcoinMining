import hashlib

nonce_limit = 100000000000
zeroes = 4

def mine(block_number,transactions,previous_hash):
    for nonce in range(nonce_limit):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f"Found Hash with Nonce:{nonce}")
            return hash_try
    return -1
block_number = 24
transactions = "40040657cc3555"
previous_hash = "3344596aadf4444"
mine(block_number,transactions,previous_hash)

