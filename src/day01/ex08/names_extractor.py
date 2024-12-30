import sys


def read_txt(file: str) -> list:
    """Функция считывает email адреса из txt-файла и возвращает их в виде списка.

    Args:
        file (str): Путь к txt-файлу.

    Returns:
        list: Список email адресов.
    """

    try:
        with open(file, encoding="utf-8") as f:
            emails = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        sys.exit(1)

    return emails


def get_credentials(emails: list) -> list:
    """Функция извлекает имя и фамилию из email адреса и возвращает их в виде списка строк.

    Args:
        emails (list): Список email адресов.

    Returns:
        list: Список строк в формате "Name\tSurname\tE-mail".
    """

    employees = []

    for email in emails:
        full_name = email.split("@")[0]
        name, surname = full_name.split(".")
        employees.append(
            f"{name.capitalize()}\t{surname.capitalize()}\t{email}"
        )

    return employees


def write_to_tsv(employees: list) -> None:
    """Функция сохраняет данные сотрудников в tsv-файл.

    Args:
        employees (list): Список строк в формате "Name\tSurname\tE-mail".
    """

    with open("employees.tsv", "w", encoding="utf-8") as f:
        f.write("Name\tSurname\tE-mail\n")
        f.write("\n".join(employees))


def main() -> None:
    """Основная функция программы."""

    if len(sys.argv) != 2:
        sys.exit(1)

    file = sys.argv[1]
    emails = read_txt(file)
    employees = get_credentials(emails)

    write_to_tsv(employees)


if __name__ == "__main__":
    main()
