def data_types() -> str:
    """Функция возвращает строку в формате списка с именами типов данных.

    Returns:
        str: Список с именами типов
    """
    # Создаем переменные разных типов
    int_type = 5
    str_type = "string"
    float_type = 3.14
    bool_type = True
    list_type = [1, 2, 3]
    dict_type = {"key": "value"}
    tuple_type = (1, 2, 3)
    set_type = {1, 2, 3}

    # Создаем список с именами типов
    types = [
        t.__name__
        for t in [
            type(int_type),
            type(str_type),
            type(float_type),
            type(bool_type),
            type(list_type),
            type(dict_type),
            type(tuple_type),
            type(set_type),
        ]
    ]
    # Формируем строку в нужном формате
    formatted_types = f"[{', '.join(types)}]"
    return formatted_types


# Вызываем функцию в случае запуска скрипта
if __name__ == "__main__":
    print(data_types())
