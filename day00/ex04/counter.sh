#!/bin/sh

# Задаем название скрипта, входного и выходного файлов
THIS_SCRIPT="$0"
INPUT_FILE="$1"
OUTPUT_FILE="hh_uniq_positions.csv"

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

# Создаем заголовки для выходного файла
if ! echo "\"name\",\"count\"" > "$OUTPUT_FILE"; then
    echo "Ошибка создания заголовков"
    exit 1
fi

# Подсчитываем уникальные значения в столбце name, сортируем по количеству
if awk -F',' '
NR > 1 { counts[$3]++ }
END {
    for (name in counts) {
        if (name != "-") {  # Пропускаем пустые значения
            printf "\"%s\",%d\n", name, counts[name]
        }
    }
}' "$INPUT_FILE" | sort -t',' -k2 -n -r >> "$OUTPUT_FILE"; then
    echo "Данные успешно подсчитаны и сохранены в ${OUTPUT_FILE}"
else
    echo "Ошибка подсчета данных"
    exit 1
fi
