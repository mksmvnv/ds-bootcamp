#!/bin/sh

# Название исполняемого скрипта, входного и выходного файлов
THIS_SCRIPT=$0
INPUT_FILE=$1
OUTPUT_FILE="hh.csv"

# Проверка числа аргументов
if [ "$#" -ne 1 ]; then
	echo "Укажите название JSON входного файла. Например: ${THIS_SCRIPT} ../ex00/hh.json"
	exit 1
fi

# Проверка наличия входного файла
if [ ! -f "$INPUT_FILE" ]; then
	echo "Файл ${INPUT_FILE} не существует"
	exit 1
fi

# Добавление заголовков CSV
if ! echo '"id","created_at","name","has_test","alternate_url"' >"$OUTPUT_FILE"; then
	echo "Ошибка добавления заголовков"
	exit 1
fi
	

# Обработка JSON с помощью jq фильтров и выгрузка данных в CSV
if jq -rf filter.jq "${INPUT_FILE}" >>"$OUTPUT_FILE"; then
	echo "Данные успешно конвертированы в CSV и сохранены в ${OUTPUT_FILE}"
else
	echo "Ошибка конвертации данных"
	exit 1
fi
