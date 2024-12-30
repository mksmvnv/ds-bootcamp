import sys


def check_letters(text: str) -> bool:
    """Функция проверяет текст на наличие кириллицы.

    Args:
        text (str): Текст для проверки.

    Returns:
        bool: True, если текст не содержит кириллицы, False в противном случае.
    """

    for char in text:
        if "а" <= char <= "я" or "А" <= char <= "Я":
            return False

    return True


def encode(text: str, shift: int) -> str:
    """Функция кодирует текст.

    Args:
        text (str): Текст для кодирования.
        shift (int): Сдвиг.

    Returns:
        str: Закодированный текст.
    """

    # Применяем только к латинским буквам
    encode_text = "".join(
        chr((ord(char) + shift - 97) % 26 + 97) if "a" <= char.lower() <= "z" else char
        for char in text
    )

    return encode_text


def decode(text: str, shift: int) -> str:
    """Функция декодирует текст.

    Args:
        text (str): Текст для декодирования.
        shift (int): Сдвиг.

    Returns:
        str: Декодированный текст.
    """

    # Применяем только к латинским буквам
    decode_text = "".join(
        chr((ord(char) - shift - 97) % 26 + 97) if "a" <= char.lower() <= "z" else char
        for char in text
    )

    return decode_text


def main() -> None:
    """Основная функция программы."""

    if len(sys.argv) != 4:
        sys.exit(1)

    convert_type = sys.argv[1]
    text = sys.argv[2]
    shift = int(sys.argv[3])

    if not check_letters(text):
        sys.exit(1)

    if convert_type == "encode":
        print(encode(text, shift))

    elif convert_type == "decode":
        print(decode(text, shift))

    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
