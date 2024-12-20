import sys


def get_company_and_stock() -> tuple:
    """Функция возвращает словари компаний и акций.

    Returns:
        tuple: Словари компаний и акций.
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

    return COMPANIES, STOCKS


def find_company_or_ticker(
    companies: dict, stocks: dict, company_or_ticker_list: list
) -> list:
    """Функция возвращает список результатов поиска компаний и акций.

    Args:
        companies (dict): Словарь компаний.
        stocks (dict): Словарь акций.
        company_or_ticker_list (list): Список компаний или акций.

    Returns:
        list: Список результатов поиска компаний и акций.
    """

    all_stocks_data = []

    companies_lower = {k.lower(): v for k, v in companies.items()}
    stocks_lower = {k.lower(): v for k, v in stocks.items()}

    for item in company_or_ticker_list:
        # Убираем пробелы и приводим к нижнему регистру
        item = item.strip().lower()

        if item in companies_lower:
            company = item.title()
            ticker = companies_lower[item]
            all_stocks_data.append(f"{company} stock price is {stocks[ticker]}")
        elif item in stocks_lower:
            ticker = item.upper()
            company = next((k for k, v in companies.items() if v.lower() == item), None)
            all_stocks_data.append(f"{ticker} is a ticker symbol for {company}")
        else:
            all_stocks_data.append(
                f"{item.title()} is an unknown company or an unknown ticker symbol"
            )

    return all_stocks_data


def main() -> None:
    """Основная функция программы."""

    if len(sys.argv) != 2:
        sys.exit()

    company_or_ticker_list = sys.argv[1].split(",")

    # Проверяем на пустые элементы
    if "" in [item.strip() for item in company_or_ticker_list]:
        sys.exit()

    companies, stocks = get_company_and_stock()
    all_stocks_data = find_company_or_ticker(companies, stocks, company_or_ticker_list)

    for item in all_stocks_data:
        print(item)


if __name__ == "__main__":
    main()
