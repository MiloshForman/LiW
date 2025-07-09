from xmlrpc.client import Boolean


def filter_by_state(source_list: list[dict], state: str='EXECUTED') -> list[dict]:
    """фильтрует словари по ключу

    принимает список словарей source_list, значение ключа state
    и возвращает список exit_list со словарями,
    у которых ключ соответствует указанному значению

    """

    exit_list = []

    for item_dict in source_list:
        if item_dict['state'] == state:
            exit_list.append(item_dict)

    return exit_list


def sort_by_date(source_list: list[dict], sort_order: bool=True) -> list[dict]:
    """сортирует ключи по дате

    принимает список словарей source_list, порядок сортировки sort_order в формате булево
    и возвращает список exit_list, отсортированный по дате в нужном порядке (по умолчанию - убывание)

    """

    exit_list = sorted(source_list, key=lambda x: x['date'], reverse=sort_order)

    return exit_list
