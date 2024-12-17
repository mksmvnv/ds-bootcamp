def read_csv(file: str) -> list:
    """Функция считывает содержимое csv-файла и возвращает его в виде списка строк.

    Args:
        file (str): Путь к csv-файлу.

    Returns:
        list: Список строк содержащих данные csv-файла.
    """

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    return file_data


def replace_comma_to_tab(file_data: list) -> list:
    """Функция заменяет запятые на табуляции вне кавычек.

    Args:
        file_data (list): Список строк, содержащих данные csv-файла.

    Returns:
        list: Список строк csv-файла с заменёнными запятыми на табуляции.
    """

    formatted_file_data = []

    for line in file_data:
        new_line = []
        quotes = False

        # Проходим по каждому символу строки и заменяем запятые на табуляции вне кавычек
        for char in line:
            if char == '"':
                quotes = not quotes
            elif char == "," and not quotes:
                new_line.append("\t")
            else:
                new_line.append(char)

        formatted_file_data.append("".join(new_line))

    return formatted_file_data


def write_csv_to_tsv(formatted_file_data: list) -> None:
    """Сохраняет содержимое csv-файла в формате tsv.

    Args:
        file_data (list): Список строк содержащих данные csv-файла.
    """

    with open("ds.tsv", "w", encoding="utf-8") as f:
        f.writelines(formatted_file_data)


def main() -> None:
    """Основная функция программы."""

    file = "ds.csv"

    file_data = read_csv(file)
    formatted_file_data = replace_comma_to_tab(file_data)

    write_csv_to_tsv(formatted_file_data)


if __name__ == "__main__":
    main()
