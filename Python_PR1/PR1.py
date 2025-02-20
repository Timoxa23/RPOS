def caesar_cipher(text, shift, direction, alphabet):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A') if alphabet == 'english' else ord('А')
            else:
                base = ord('a') if alphabet == 'english' else ord('а')
            shift = shift % len(alphabet)
            if direction == 'decrypt':
                shift = -shift
            result += chr((ord(char) - base + shift) % len(alphabet) + base)
        else:
            result += char
    return result

def get_alphabet(language):
    if language == 'english':
        return 'abcdefghijklmnopqrstuvwxyz'
    elif language == 'russian':
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

if __name__ == "__main__":
    direction = input("Введите направление (encrypt/decrypt): ").strip().lower()
    language = input("Введите язык алфавита (english/russian): ").strip().lower()
    shift = int(input("Введите шаг сдвига: "))
    text = input("Введите текст для обработки: ")

    alphabet = get_alphabet(language)
    result = caesar_cipher(text, shift, direction, alphabet)
    print(f"Результат: {result}")
