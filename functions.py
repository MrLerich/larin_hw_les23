import re
from typing import List


def filter_query(param: str, data: List[str]) -> List[str]:
    """Фильтрует данные."""
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: List[str]) -> List[str]:
    """Получает номер колонки и выводит списком данные этой колонки."""
    col_number = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data: List[str], *args, **kwargs) -> List:
    """Создает список из уникальных позиций."""
    return list(set(data))


def sort_query(param: str, data: List[str]) -> List[str]:
    """ Сортирует данные."""
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: List[str]) -> List[str]:
    """Создает список позиций в заданном количестве."""
    limit = int(param)
    return list(data)[:limit]


def search_pic(param: str, data: List[str]) -> List[str]:
    regex = re.compile(param)
    return list(filter(lambda y: regex.search(y), data))
