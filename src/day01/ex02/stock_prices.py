import sys


def get_stock_price(company: str) -> float | str:
    """Функция возвращает цену акции компании.

    Args:
        company (str): Название компании.

    Returns:
        float: Цена акции.
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

    # Получаем тикер компании
    ticker = COMPANIES.get(company)

    # Отрабатываем случай, когда компания не нашлась
    if not ticker:
        return "Unknown company"

    return STOCKS[ticker]


def main() -> None:
    """Основная функция программы."""

    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        sys.exit(1)

    # Считываем имя компании и приводим первую символ в верхний регистр
    company = sys.argv[1].capitalize()

    # Получаем и выводим цену акций
    print(get_stock_price(company))


if __name__ == "__main__":
    main()
