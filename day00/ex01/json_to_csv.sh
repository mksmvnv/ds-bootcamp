#!/bin/sh

# Название исполняемого скрипта, входного и выходного файлов
SCRIPT=$0
INPUT_FILE=$1
OUTPUT_FILE="hh.csv"

# Проверка числа аргументов
if [ "$#" -ne 1 ]; then
  echo "Укажите название JSON входного файла. Например: ${SCRIPT} ../ex00/hh.json"
  exit 1
fi

# Проверка наличия входного файла
if [ ! -f $INPUT_FILE ]; then
  echo "Файл ${INPUT_FILE} не существует"
  exit 1
fi

# Проверка наличия выходного файла
if [ ! -f $OUTPUT_FILE ]; then
  touch $OUTPUT_FILE
fi

# Генерация заголовков CSV
echo '"id","created_at","name","has_test","alternate_url"' > $OUTPUT_FILE

# Обработка JSON с помощью jq и выгрузка данных в CSV
jq -rf filter.jq "${INPUT_FILE}" >> $OUTPUT_FILE

# Проверка успешности выполнения запроса
if [ $? -eq 0 ]; then
  echo "Данные успешно конвертированы в CSV и сохранены в ${OUTPUT_FILE}"
else
  echo "Ошибка конвертации данных"
  exit 1
fi