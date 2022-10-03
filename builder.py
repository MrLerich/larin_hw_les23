import functions

CMD_TO_FUNCTION = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query
}

FILE_NAME = 'data/apache_logs.txt'


def build_query(cmd, param, data):
    """Создает запросы"""
    if data is None:
        with open(FILE_NAME) as f:
            prepare_data = list(map(lambda x: x.strip(), f))
    else:
        prepare_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepare_data)
