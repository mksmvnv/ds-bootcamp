def convert_to_dict() -> dict:
    """Функция преобразует список кортежей в словарь, где ключ - это число, а значение - список стран.

    Returns:
        dict: Словарь, где ключ - это число, а значение - список стран.
    """

    list_of_tuples = [
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

    converted_dict = {}

    # Преобразуем список кортежей в словарь, где ключом будет число,
    # А значением список стран с этим числом
    for country, num in list_of_tuples:
        if num not in converted_dict:
            converted_dict[num] = []
        converted_dict[num].append(country)

    return converted_dict


def format_dict(converted_dict: dict) -> list:
    """Функция преобразует словарь в строки, где ключ - это число, а значение - страна.

    Args:
        result_dict (dict): Словарь, где ключ - это число, а значение - список стран.

    Returns:
        list: Список отформатированных строк.
    """

    formatted_list = []

    for num, countries in converted_dict.items():
        for country in countries:
            formatted_list.append(f"'{num}' : '{country}'")

    return formatted_list


def main() -> None:
    """Основная функция программы."""

    converted_dict = convert_to_dict()
    formatted_list = format_dict(converted_dict)

    for item in formatted_list:
        print(item)


if __name__ == "__main__":
    main()
