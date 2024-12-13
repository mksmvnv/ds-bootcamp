#!/bin/sh

# Задаем название скрипта и входного файла
THIS_SCRIPT="$0"
INPUT_FILE="$1"

# Проверяем число аргументов
if [ "$#" -ne 1 ]; then
    echo "Укажите название CSV входного файла. Например: ${THIS_SCRIPT} ../ex03/hh_positions.csv"
    exit 1
fi

# Проверяем наличие входного файла
if [ ! -f "$INPUT_FILE" ]; then
    echo "Файл ${INPUT_FILE} не существует"
    exit 1
fi

# Считываем заголовки из входного файла
if ! HEADER=$(head -n 1 "$INPUT_FILE"); then
    echo "Ошибка чтения заголовков"
    exit 1
fi

# Разбиваем файл на части по дате
if awk -F',' -v header="$HEADER" '
NR == 1 { next }  # Пропускаем заголовки
{
    # Пропускаем кавычки только в части даты, не трогаем данные
    date = substr($2, 2, index($2, "T") - 2);  # Отрезаем кавычки вокруг даты

    # Проверяем, был ли уже создан файл для данной даты
    if (!(date in files)) {  
        files[date] = 1;  # Помечаем, что файл для этой даты создан
        # Добавляем заголовки в новый файл для даты
        print header > date".csv";  
    }

    # Добавляем строку данных в файл для этой даты
    print $0 >> date".csv";  
}' "$INPUT_FILE"; then
    echo "Данные успешно разделены по датам и сохранены в отдельные файлы"
else
    echo "Ошибка разделения данных по датам"
    exit 1
fi