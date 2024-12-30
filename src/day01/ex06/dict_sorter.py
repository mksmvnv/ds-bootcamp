def get_list_of_tuples() -> list:
    """Функция возвращает список стран с номерами в кортежах.

    Returns:
        list: Список стран с номерами.
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

    return list_of_tuples


def convert_to_dict(list_of_tuples: list) -> dict:
    """Функция преобразует список кортежей в словарь, где ключ - это число, а значение - список стран.

    Args:
        list_of_tuples (list): Список стран с номерами.

    Returns:
        dict: Словарь, где ключ - это число, а значение - список стран.
    """

    converted_dict = {}

    # Преобразуем список кортежей в словарь, где ключом будет число,
    # А значением список стран с этим числом
    for country, num in list_of_tuples:
        if country not in converted_dict:
            converted_dict[country] = []
        converted_dict[country].append(num)

    return converted_dict


def sort_dict(converted_dict: dict) -> dict:
    """
    Функция сортирует страны по убыванию номеров.
    Если номера одинаковые, применяется сортировка по алфавиту.

    Args:
        converted_dict (dict): Словарь, где ключ - это число, а значение - список стран.

    Returns:
        dict: Словарь, где ключ - это число, а значение - список стран.
    """

    sorted_dict = dict(
        sorted(converted_dict.items(), key=lambda x: (-int(x[1][0]), x[0]))
    )

    return sorted_dict


def main() -> None:
    """Основная функция программы."""

    list_of_tuples = get_list_of_tuples()
    converted_dict = convert_to_dict(list_of_tuples)
    sorted_dict = sort_dict(converted_dict)

    for k, _ in sorted_dict.items():
        print(k)


if __name__ == "__main__":
    main()
