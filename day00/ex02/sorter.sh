#!/bin/sh

# Название исполняемого скрипта и выходного файлов
SCRIPT=$0
INPUT_FILE=$1
OUTPUT_FILE="hh_sorted.csv"

# Проверка числа аргументов
if [ "$#" -ne 1 ]; then
  echo "Укажите название CSV входного файла. Например: ${SCRIPT} ../ex01/hh.csv"
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

# Сохранение первой строки с заголовками
head -n 1 $INPUT_FILE > $OUTPUT_FILE

# Сортировка со 2 строки CSV файла по created_at и id в порядке возрастания
tail -n +2 $INPUT_FILE | sort -t "," -k 2,2 -k 1,1n >> $OUTPUT_FILE

# Проверка успешности выполнения запроса
if [ $? -eq 0 ]; then
  echo "Данные успешно отсортированы и сохранены в ${OUTPUT_FILE}"
else
  echo "Ошибка сортировки данных"
  exit 1
fi