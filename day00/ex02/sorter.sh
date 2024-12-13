#!/bin/sh

# Название исполняемого скрипта, входного и выходного файлов
THIS_SCRIPT=$0
INPUT_FILE=$1
OUTPUT_FILE="hh_sorted.csv"

# Проверка числа аргументов
if [ "$#" -ne 1 ]; then
	echo "Укажите название CSV входного файла. Например: ${THIS_SCRIPT} ../ex01/hh.csv"
	exit 1
fi

# Проверка наличия входного файла
if [ ! -f "$INPUT_FILE" ]; then
	echo "Файл ${INPUT_FILE} не существует"
	exit 1
fi

# Сохранение первой строки с заголовками
if ! head -n 1 "$INPUT_FILE" >"$OUTPUT_FILE"; then
	echo "Ошибка сохранения заголовков"
	exit 1
fi

# Сортировка со 2 строки CSV файла по created_at и id в порядке возрастания
if tail -n +2 "$INPUT_FILE" | sort -t "," -k 2,2 -k 1,1n >>"$OUTPUT_FILE"; then
	echo "Данные успешно отсортированы и сохранены в ${OUTPUT_FILE}"
else
	echo "Ошибка сортировки данных"
	exit 1
fi
