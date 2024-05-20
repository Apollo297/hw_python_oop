# Модуль фитнес-трекера

Данный программный модуль решает задачу расчета различных характеристик тренировок, таких как дистанция, средняя скорость и количество затраченных калорий, для трех типов физических упражнений: бег, спортивная ходьба и плавание. Он также формирует оповещения с информацией о выполненной тренировке.

### Потенциальные сценарии использования:

1. **Персональные тренировки**:
   Модуль может быть использован фитнес-приложениями или тренажерами для анализа и предоставления результатов тренировок пользователю. Например, приложение для бега может собрать данные о действиях пользователя (шаги), времени тренировки и весе, а затем использовать этот модуль для расчета сожженных калорий и средней скорости, предоставляя пользователю подробную информацию о тренировке.

2. **Приложения для диет и здоровья**:
   Приложения, отслеживающие калории и общее состояние здоровья, могут применять этот модуль для учета физических нагрузок пользователей. Это поможет создавать более точные рекомендации по питанию и физическим активностям.

## Установка:
Если Python не установлен, скачайте и установите его с [официального сайта](https://www.python.org/downloads/).

Клонировать репозиторий и перейти в него в командной строке:
```python
git clone https://github.com/Apollo297/hw_python_oop.git 
```
```python
cd hw_python_oop
```
Cоздать и активировать виртуальное окружение:
```python
python3 -m venv env
```
```python
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```python
python3 -m pip install --upgrade pip
```
```python
pip install -r requirements.txt
```
Запустите скрипт:
```python
python homework.py
```
## Пример вывода:
Тип тренировки: Swimming; Длительность: 1.000 ч.; Дистанция: 0.993 км; Ср. скорость: 0.993 км/ч; Потрачено ккал: 279.024.</br>
Тип тренировки: Running; Длительность: 1.000 ч.; Дистанция: 9.750 км; Ср. скорость: 9.750 км/ч; Потрачено ккал: 1516.500.</br>
Тип тренировки: SportsWalking; Длительность: 1.000 ч.; Дистанция: 5.850 км; Ср. скорость: 5.850 км/ч; Потрачено ккал: 425.250.

## Стек:
1. ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) - Основной язык программирования;
2. ![Dataclasses](https://img.shields.io/badge/Dataclasses-555555?style=for-the-badge) - Для создания классов;
3. ![Standard Library](https://img.shields.io/badge/Standard%20Library-555555?style=for-the-badge) - Для работы с вводом/выводом и обработки данных.
