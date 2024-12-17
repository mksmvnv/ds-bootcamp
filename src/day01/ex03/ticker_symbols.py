import sys


def get_company_and_stock(ticker: str) -> str:
    """Функция возвращает название компании и цену акции.

    Args:
        ticker (str): Тикер компании.

    Returns:
        str: Название компании и цену акции.
    """

    COMPANIES = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "Tesla": "TSLA",
        "Nokia": "NOK",
    }

    STOCKS = {
        "AAPL": 287.73,
        "MSFT": 173.79,
        "NFLX": 416.90,
        "TSLA": 724.88,
        "NOK": 3.37,
    }

    # Получаем название компании и цену акции
    # Отрабатываем случай, когда компания не нашлась
    company_stock = next(
        (
            f"{key} {STOCKS[ticker]}"
            for key, value in COMPANIES.items()
            if value == ticker
        ),
        "Unknown ticker",
    )

    return company_stock


def main() -> None:
    """Основная функция программы."""

    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        sys.exit(1)

    # Считываем тикер и приводим к верхнему регистру
    ticker = sys.argv[1].upper()

    # Получаем и выводим название компании и цену акции
    print(get_company_and_stock(ticker))


if __name__ == "__main__":
    main()
