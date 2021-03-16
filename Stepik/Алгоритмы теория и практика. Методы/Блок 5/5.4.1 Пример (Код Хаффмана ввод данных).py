def huffman_encode(s):
    return {ch: ch for ch in s}


def main():
    s = input()  # строка ввода не длинне, чем 10^4, поэтому ввод можно использовать любой
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))  # выводим количество символов строки и длину закодированной строки
    for ch in sorted(code):  # для удобство обходить символы будем в алфавитном порядке
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()
