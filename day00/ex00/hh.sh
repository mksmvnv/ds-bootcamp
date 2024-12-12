#!/bin/sh

# Название испольняемого скрипта и выходного файлов
SCRIPT=$0
OUTPUT_FILE="hh.json"

# Проверка числа аргументов
if [ "$#" -ne 1 ]; then
  echo "Укажите название вакансии. Например: ${SCRIPT} \"Data Scientist\""
  exit 1
fi

# Проверка наличия выходного файла
if [ ! -f $OUTPUT_FILE ]; then
  touch $OUTPUT_FILE
fi

# Название вакансии с заменой пробелов на код %20 для корректной выгрузки данных
VACANCY_NAME=$(echo "$1" | sed 's/ /%20/g')

# Кол-во страниц
PAGE_COUNT=20

# URL API для получения вакансий
API_URL="https://api.hh.ru/vacancies"

# Запрос к API для получения первых 20 вакансий по запросу
curl -s "${API_URL}?text=%22${VACANCY_NAME}%22&per_page=${PAGE_COUNT}" | \
  jq '.' > $OUTPUT_FILE

# Проверка успешности выполнения запроса
if [ $? -eq 0 ]; then
  echo "Данные о вакансиях успешно сохранены в файл ${OUTPUT_FILE}"
else
  echo "Ошибка при запросе данных"
  exit 1
fi


