def filter_by_state(source_list: list[dict], state='EXECUTED') -> list[dict]:
    """принимает список словарей со значением ключа, и возвращает список со словарями, у которых ключ соответствует указанному значению"""

    exit_list = []

    for item_dict in source_list:
        if item_dict['state'] == state:
            exit_list.append(item_dict)

    return exit_list


def sort_by_date(source_list: list[dict], sort_order=True) -> list[dict]:
    """принимает список словарей и возвращает список, отсортированный по дате в нужном порядке"""

    exit_list = sorted(source_list, key=lambda x: x['date'], reverse=sort_order)

    return exit_list
