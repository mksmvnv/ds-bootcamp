import sys


def get_employee_name(file: str, email: str) -> str:
    """Функция возвращает имя сотрудника.

    Args:
        file (str): Путь к tsv-файлу.
        email (str): Email сотрудника.

    Returns:
        str: Имя сотрудника.
    """

    name = None

    try:
        with open(file, encoding="utf-8") as f:
            next(f)
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) > 2 and parts[2] == email:
                    name = parts[0]
                    break
    except FileNotFoundError:
        sys.exit(1)

    if name is None:
        sys.exit(1)

    return name


def get_paragraph_letter(name: str) -> str:
    """Функция возвращает письмо с приветствием.

    Args:
        name (str): Имя сотрудника.

    Returns:
        str: Письмо с приветствием.
    """

    paragraph_letter = (
        f"Dear {name}, welcome to our team. "
        f"We are sure that it will be a pleasure to work with you. "
        f"That’s a precondition for the professionals that our company hires."
    )

    return paragraph_letter


def main() -> None:
    """Основная функция программы."""

    if len(sys.argv) != 2:
        sys.exit(1)

    file = "employees.tsv"
    email = sys.argv[1]
    name = get_employee_name(file, email)
    paragraph_letter = get_paragraph_letter(name)

    print(paragraph_letter)


if __name__ == "__main__":
    main()
