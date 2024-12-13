#!/bin/sh

# Название исполняемого скрипта, входного, выходного и временного файлов
THIS_SCRIPT=$0
INPUT_FILE=$1
OUTPUT_FILE="hh_positions.csv"
TEMP_FILE="temp_positions.csv"

# Ключевые слова для поиска
KEYWORDS="Junior|Middle|Senior"

# Проверка числа аргументов
if [ "$#" -ne 1 ]; then
    echo "Укажите название CSV входного файла. Например: ${THIS_SCRIPT} ../ex02/hh_sorted.csv"
    exit 1
fi

# Проверка наличия входного файла
if [ ! -f "$INPUT_FILE" ]; then
    echo "Файл ${INPUT_FILE} не существует"
    exit 1
fi

# Обработка входного файла
if ! {
    # Считываем заголовок и записываем его во временный файл
    IFS= read -r HEADER
    echo "$HEADER" >"$TEMP_FILE"

    # Обрабатываем каждую строку
    while IFS= read -r LINE; do
        # Заменяем запятую на символ | в случае, если is_quotes = 1
        # Чтобы awk не рассматривал запятые внутри ковычек как разделитель
        # Случай: "Data Scientist/Разработчик машинного обучения (ML, NLM, LLM)"
        CLEANED_LINE=$(
            echo "$LINE" | awk -v RS='' '
      BEGIN { FS=""; OFS="" }
      {
        in_quotes = 0;
        for (i = 1; i <= NF; i++) {
          if ($i == "\"") { in_quotes = !in_quotes }
          if ($i == "," && in_quotes) { $i = "|" }
        }
        print
      }'
        )

        # Извлекаем название вакансии
        POSITION_NAME=$(echo "$CLEANED_LINE" | awk -F',' '{print $3}' | sed 's/|/,/g')

        # Ищем ключевые слова из KEYWORDS в названии вакансии
        MATCH=$(echo "$POSITION_NAME" | grep -Eo "$KEYWORDS" | paste -sd'/')

        # Если ключевые слова не найдены, устанавливаем значение "-"
        if [ -z "$MATCH" ]; then
            MATCH="-"
        fi

        # Заменяем название вакансии на найденные ключевые слова
        FINAL_LINE=$(echo "$CLEANED_LINE" | awk -v newName="$MATCH" -F',' 'BEGIN {OFS=","} {$3=newName; print}' | sed 's/|/,/g')

        # Записываем результат во временный файл
        echo "$FINAL_LINE" >>"$TEMP_FILE"
    done
} <"$INPUT_FILE"; then
    echo "Ошибка обработки данных"
    exit 1
fi

if ! head -n 1 "$TEMP_FILE" >"$OUTPUT_FILE"; then
	echo "Ошибка сохранения заголовков"
	exit 1
fi

# Сортируем временный файл (исключая заголовок) и сохраняем результат
if ! tail -n +2 "$TEMP_FILE" | sort -t "," -k 2,2 -k 1,1n >>"$OUTPUT_FILE"; then
    echo "Ошибка сортировки данных"
    exit 1
fi

# Удаляем временный файл
if rm "$TEMP_FILE"; then
    echo "Данные успешно заменены и сохранены в ${OUTPUT_FILE}"
else
    echo "Ошибка удаления временного файла"
    exit 1
fi
