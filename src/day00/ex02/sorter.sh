#!/bin/sh

# Задаем название скрипта, входного и выходного файлов
THIS_SCRIPT="$0"
INPUT_FILE="$1"
OUTPUT_FILE="hh_sorted.csv"

# Проверяем число аргументов
if [ "$#" -ne 1 ]; then
	echo "Укажите название CSV входного файла. Например: ${THIS_SCRIPT} ../ex01/hh.csv"
	exit 1
fi

# Проверяем наличие входного файла
if [ ! -f "$INPUT_FILE" ]; then
	echo "Файл ${INPUT_FILE} не существует"
	exit 1
fi

# Сохраняем заголовки из входного файла
if ! head -n 1 "$INPUT_FILE" >"$OUTPUT_FILE"; then
	echo "Ошибка сохранения заголовков"
	exit 1
fi

# Сортируем по столбцам created_at и id по возрастанию
if tail -n +2 "$INPUT_FILE" | sort -t "," -k 2,2 -k 1,1n >>"$OUTPUT_FILE"; then
	echo "Данные успешно отсортированы и сохранены в ${OUTPUT_FILE}"
else
	echo "Ошибка сортировки данных"
	exit 1
fi
