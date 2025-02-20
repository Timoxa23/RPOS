
def capitalize_string(s):
    return ' '.join(word.capitalize() if word.isalpha() else word for word in s.split())
s = input("Введите строку: ")
print(capitalize_string(s))
