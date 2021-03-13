from AES import AES
from Key_Scheduling import KeyScheduling
from io import StringIO


def handle_encryption(aes_obj):

    cypher_text = []
    total_time = 0
    encrypted_text = ""
    plain_text = input()
    with StringIO(plain_text) as f:
        while True:
            chunk = f.read(16)

            if not chunk:
                break
            aes_obj.take_input(chunk)
            total_time += aes_obj.encryption()
            cypher_text.append(aes_obj.get_state_mat())
            encrypted_text += aes_obj.print_text()
    print("Encrypted TEXT: ", encrypted_text)
    return cypher_text, total_time


def handle_decryption(cypher_text, aes_obj):
    total_time = 0
    print_text = ""
    for count in range(0, len(cypher_text)):
        aes_obj.set_state_mat(cypher_text[count])
        total_time += aes_obj.decryption()
        print_text += aes_obj.print_text()
    print("Decrypted TEXT: ", print_text)
    return total_time


if __name__ == "__main__":

    sch = KeyScheduling()
    scheduling_time = sch.scheduler()
    round_keys = sch.get_key()

    print("Round Keys: ", round_keys)
    aes = AES(round_keys)
    cypher_text, encrypt_time = handle_encryption(aes)

    decrypt_time = handle_decryption(cypher_text, aes)

    print("Key Scheduling Time ", scheduling_time)
    print("Encryption Time ", encrypt_time)
    print("Decryption Time ", decrypt_time)
