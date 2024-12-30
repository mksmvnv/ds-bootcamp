import sys


def get_audience() -> tuple:
    """Функция возвращает кортеж клиентов, участников и получателей.

    Returns:
        tuple: Кортеж клиентов, участников и получателей.
    """

    clients = [
        "andrew@gmail.com",
        "jessica@gmail.com",
        "ted@mosby.com",
        "john@snow.is",
        "bill_gates@live.com",
        "mark@facebook.com",
        "elon@paypal.com",
        "jessica@gmail.com",
    ]
    participants = [
        "walter@heisenberg.com",
        "vasily@mail.ru",
        "pinkman@yo.org",
        "jessica@gmail.com",
        "elon@paypal.com",
        "pinkman@yo.org",
        "mr@robot.gov",
        "eleven@yahoo.com",
    ]
    recipients = ["andrew@gmail.com", "jessica@gmail.com", "john@snow.is"]

    audience = (clients, participants, recipients)

    return audience


def participants_not_in_clients(participants: list, clients: list) -> list:
    """Функция возвращает список участников, которых нет в клиентах.

    Args:
        participants (list): Список участников.
        clients (list): Список клиентов.

    Returns:
        list: Список участников, которых нет в клиентах.
    """

    not_clients = [
        participant
        for participant in participants
        if participant not in clients
    ]

    return not_clients


def clients_not_in_recipients(clients: list, recipients: list) -> list:
    """Функция возвращает список клиентов, которых нет в получателях.

    Args:
        clients (list): Список клиентов.
        recipients (list): Список получателей.

    Returns:
        list: Список клиентов, которых нет в получателях.
    """

    not_recipients = [client for client in clients if client not in recipients]

    return not_recipients


def clients_not_in_participants(clients: list, participants: list) -> list:
    """Функция возвращает список клиентов, которых нет в участниках.

    Args:
        clients (list): Список клиентов.
        participants (list): Список участников.

    Returns:
        list: Список клиентов, которых нет в участниках.
    """

    not_participants = [
        client for client in clients if client not in participants
    ]

    return not_participants


def main() -> None:
    """Основная функция программы."""

    if len(sys.argv) != 2:
        sys.exit(1)

    if sys.argv[1] == "call_center":
        print(clients_not_in_recipients(get_audience()[0], get_audience()[2]))

    elif sys.argv[1] == "potential_clients":
        print(
            participants_not_in_clients(get_audience()[1], get_audience()[0])
        )

    elif sys.argv[1] == "loly_program":
        print(
            clients_not_in_participants(get_audience()[0], get_audience()[1])
        )

    else:
        print("Unknown command")
        sys.exit(1)


if __name__ == "__main__":
    main()
