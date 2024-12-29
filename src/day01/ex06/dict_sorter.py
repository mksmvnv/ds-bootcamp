def get_countries() -> list:
    """Функция возвращает список стран с номерами в кортежах.

    Returns:
        list: Список стран с номерами.
    """

    countries = [
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

    return countries


def convert_to_dict(countries: list) -> dict:
    """Функция преобразует список кортежей в словарь, где ключ - это число, а значение - список стран.

    Args:
        countries (list): Список стран с номерами.

    Returns:
        dict: Словарь, где ключ - это число, а значение - список стран.
    """

    converted_dict = {}

    # Преобразуем список кортежей в словарь, где ключом будет число,
    # А значением список стран с этим числом
    for country, num in countries:
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

    countries = get_countries()
    converted_dict = convert_to_dict(countries)
    sorted_dict = sort_dict(converted_dict)

    for k, _ in sorted_dict.items():
        print(k)


if __name__ == "__main__":
    main()
