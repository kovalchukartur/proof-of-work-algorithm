import hashlib


def proof_of_work(input_data: str):
    nonce = 0
    hashed_value = ''

    while not hashed_value.startswith('0000'):
        nonce += 1
        hashed_value = calc_hash(input_data, nonce)

    return nonce


def is_valid_proof(input_data, nonce):
    hash_value = calc_hash(input_data, nonce)
    print("Hash for verification: ", hash_value)
    return hash_value.startswith('0000')


def calc_hash(input_data, nonce):
    return hashlib.sha256(f"{input_data}{nonce}".encode('utf-8')).hexdigest()


data = 'artur'
found_nonce = proof_of_work(data)
print("Hash:", found_nonce, "Is valid:", is_valid_proof(data, found_nonce))
