from xmlrpc.client import Boolean
import re


def filter_by_state(source_list: list[dict], state: str='EXECUTED') -> list[dict]:
    """фильтрует словари по ключу

    принимает список словарей source_list, значение ключа state
    и возвращает список exit_list со словарями,
    у которых ключ соответствует указанному значению

    """

    exit_list = list(filter(lambda operation: operation.get("state") == state, source_list))

    return exit_list


def sort_by_date(source_list: list[dict], sort_order: bool=True) -> list[dict]:
    """сортирует ключи по дате

    принимает список словарей source_list, порядок сортировки sort_order в формате булево
    и возвращает список exit_list, отсортированный по дате в нужном порядке (по умолчанию - убывание)

    """

    for l_dict in source_list:
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}\w\d{2}:\d{2}:\d{2}\.\d{6}', l_dict['date']):
            continue
        else:
            return 'Некорректная дата'

    exit_list = sorted(source_list, key=lambda x: x['date'], reverse=sort_order)

    return exit_list
