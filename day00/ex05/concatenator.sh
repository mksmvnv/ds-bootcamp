#!/bin/sh

# Задаем название скрипта, входных и выходного файлов
THIS_SCRIPT="$0"
INPUT_FILES="$*"
OUTPUT_FILE="hh_positions.csv"

# Проверяем число аргументов
if [ "$#" -lt 1 ]; then
	echo "Укажите название минимум одного CSV входного файла"
	echo "Например: ${THIS_SCRIPT} ./2024-11-22.csv ./2024-11-25.csv"
	exit 1
fi

# Проверяем наличие всех входных файлов
for FILE in $INPUT_FILES; do
	if [ ! -f "$FILE" ]; then
		echo "Файл ${FILE} не существует"
		exit 1
	fi
done

# Задаем заголовки из первого входного файла
if ! HEADER=$(head -n 1 "$1"); then
	echo "Ошибка создания заголовков"
	exit 1
fi

# Создаем выходный файл с заголовками
if ! echo "$HEADER" >"$OUTPUT_FILE"; then
	echo "Ошибка создания выходного файла"
	exit 1
fi

# Объединяем остальные файлы, исключая заголовки
for FILE in $INPUT_FILES; do
	tail -n +2 "$FILE" >>"$OUTPUT_FILE"
done

echo "Файлы успешно объединены в ${OUTPUT_FILE}"
