from secrets import token_bytes


def bytes_to_int(bites):
    return int.from_bytes(bites, "big")


def random_key(length):
    return bytes_to_int(token_bytes(length))


def encrypt(string):
    string_bytes = string.encode()
    string_int = bytes_to_int(string_bytes)
    dummy = random_key(len(string_bytes))
    return dummy, string_int ^ dummy


def decrypt(k1, k2):
    decrypted = k1 ^ k2
    # let's avoid off by one
    tmp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return tmp.decode()


if __name__ == "__main__":
    k1, k2 = encrypt("This is a test.")
    print(k1, k2)
    print(decrypt(k1, k2))
