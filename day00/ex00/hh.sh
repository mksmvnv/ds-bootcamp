#!/bin/sh

# Название испольняемого скрипта и выходного файла
THIS_SCRIPT=$0
OUTPUT_FILE="hh.json"

# API URL адрес для получения списка вакансий
API_URL="https://api.hh.ru/vacancies"

# Название вакансий с заменой пробелов на код %20 для корректной выгрузки данных
POSITION_NAME=$(echo "$1" | sed 's/ /%20/g')

# Количество вакансий
POSITION_COUNT=$2

# Проверка числа аргументов (2 аргумента)
if [ "$#" -ne 2 ]; then
	echo "Укажите название вакансии и требуемое количество. Например: ${THIS_SCRIPT} \"Data Scientist\" 20"
	exit 1
fi

# Проверка количества вакансий
if [ "$POSITION_COUNT" -lt 1 ]; then
	echo "Количество вакансий должно быть больше 0"
	exit 1
fi

# Запрос к API для получения указанного количества вакансий в JSON формате через jq
if curl -s "${API_URL}?text=%22${POSITION_NAME}%22&per_page=${POSITION_COUNT}" |
	jq '.' >"$OUTPUT_FILE"; then
	echo "Данные о вакансиях успешно сохранены в файл ${OUTPUT_FILE}"
else
	echo "Произошла ошибка при получении данных о вакансиях"
	exit 1
fi
