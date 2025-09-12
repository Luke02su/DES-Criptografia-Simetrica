# DES simplificado com saída em hexadecimal

def xor(a, b):
    """Faz XOR entre duas strings de bits"""
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

def string_to_bits(s):
    """Converte cada caractere em 8 bits"""
    return ''.join(format(ord(c), '08b') for c in s)

def bits_to_string(b):
    """Converte bits de volta para caracteres"""
    chars = [chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8)]
    return ''.join(chars)

def pad(text):
    """Adiciona padding até 8 caracteres"""
    pad_len = 8 - (len(text) % 8)
    return text + chr(pad_len) * pad_len

def unpad(text):
    """Remove padding"""
    pad_len = ord(text[-1])
    return text[:-pad_len]

def generate_subkeys(key):
    """Gera 16 subchaves iguais (simplificação)"""
    key_bits = string_to_bits(key.ljust(8)[:8])
    return [key_bits] * 16

def F(right, subkey):
    """Função F simplificada"""
    return xor(right, subkey)

def des_block_encrypt(block, subkeys):
    """Cifra um bloco de 64 bits"""
    L, R = block[:32], block[32:]
    for k in subkeys:
        L, R = R, xor(L, F(R, k))
    return R + L

def des_block_decrypt(block, subkeys):
    """Decifra um bloco de 64 bits"""
    L, R = block[:32], block[32:]
    for k in reversed(subkeys):
        L, R = R, xor(L, F(R, k))
    return R + L

def des_encrypt(message, key):
    message = pad(message)
    subkeys = generate_subkeys(key)
    encrypted_bits = ''
    for i in range(0, len(message), 8):
        block = string_to_bits(message[i:i+8])
        encrypted_bits += des_block_encrypt(block, subkeys)
    # Converte bits para hexadecimal legível
    hex_result = hex(int(encrypted_bits, 2))[2:]
    hex_result = hex_result.zfill((len(encrypted_bits) // 4))
    return hex_result

def des_decrypt(cipher_hex, key):
    # Converte hexadecimal de volta para bits
    cipher_bits = bin(int(cipher_hex, 16))[2:].zfill(len(cipher_hex)*4)
    subkeys = generate_subkeys(key)
    decrypted = ''
    for i in range(0, len(cipher_bits), 64):
        block = cipher_bits[i:i+64]
        decrypted += bits_to_string(des_block_decrypt(block, subkeys))
    return unpad(decrypted)

# ===== Interface simples =====
def main():
    print("=== DES Simplificado Final ===")
    opcao = input("Escolha a opção: [1] Cifrar  [2] Decifrar: ")

    chave = input("Digite a chave (até 8 caracteres): ")

    if opcao == "1":
        mensagem = input("Digite a mensagem a ser cifrada: ")
        cifrada = des_encrypt(mensagem, chave)
        print("\nMensagem cifrada (hex):", cifrada)

    elif opcao == "2":
        cifrada = input("Digite a mensagem cifrada (hex): ")
        try:
            decifrada = des_decrypt(cifrada, chave)
            print("\nMensagem decifrada:", decifrada)
        except Exception as e:
            print("Erro ao decifrar. Verifique a chave e a mensagem.")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
