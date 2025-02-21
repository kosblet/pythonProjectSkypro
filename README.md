# Bank Operations Widget

## Описание проекта
Этот проект представляет собой виджет для работы с банковскими операциями клиента. Он включает функции для фильтрации и сортировки операций.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone  
Перейдите в директорию проекта:


cd your_project
Создайте и активируйте виртуальное окружение:
#
python -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
Установите зависимости:

pip install -r requirements.txt

## Использование
Пример использования функций:

```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered = filter_by_state(operations, 'EXECUTED')
sorted_operations = sort_by_date(operations)
