def get_tuple_list() -> list:
    """Функция возвращает список кортежей.

    Returns:
        list: Список кортежей.
    """

    tuple_list = [
        ("Russia", "25"),
        ("France", "132"),
        ("Germany", "132"),
        ("Spain", "178"),
        ("Italy", "162"),
        ("Portugal", "17"),
        ("Finland", "3"),
        ("Hungary", "2"),
        ("The Netherlands", "28"),
        ("The USA", "610"),
        ("The United Kingdom", "95"),
        ("China", "83"),
        ("Iran", "76"),
        ("Turkey", "65"),
        ("Belgium", "34"),
        ("Canada", "28"),
        ("Switzerland", "26"),
        ("Brazil", "25"),
        ("Austria", "14"),
        ("Israel", "12"),
    ]

    return tuple_list


def convert_to_dict(tuple_list: list) -> dict:
    """Функция преобразует список кортежей в словарь, где ключ - это число, а значение - список стран.

    Args:
        tuple_list (list): Список кортежей.

    Returns:
        dict: Словарь, где ключ - это число, а значение - список стран.
    """

    converted_dict = {}

    # Преобразуем список кортежей в словарь, где ключом будет число,
    # А значением список стран с этим числом
    for country, num in tuple_list:
        if num not in converted_dict:
            converted_dict[num] = []
        converted_dict[num].append(country)

    return converted_dict


def convert_to_list(converted_dict: dict) -> list:
    """Функция преобразует словарь в строки, где ключ - это число, а значение - страна.

    Args:
        converted_dict (dict): Словарь, где ключ - это число, а значение - список стран.

    Returns:
        list: Список отформатированных строк.
    """

    converted_list = []

    for num, countries in converted_dict.items():
        for country in countries:
            converted_list.append(f"'{num}' : '{country}'")

    return converted_list


def main() -> None:
    """Основная функция программы."""

    tuple_list = get_tuple_list()

    converted_dict = convert_to_dict(tuple_list)
    converted_list = convert_to_list(converted_dict)

    for item in converted_list:
        print(item)


if __name__ == "__main__":
    main()
