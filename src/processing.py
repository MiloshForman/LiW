def filter_by_state(source_list: list[dict], state='EXECUTED') -> list[dict]:
    """принимает список словарей со значением ключа, и возвращает список со словарями, у которых ключ соответствует указанному значению"""

    exit_list = []

    for item_dict in source_list:
        if item_dict['state'] == state:
            exit_list.append(item_dict)

    return exit_list


