def get_val(collection: dict, key: str, *args: str):
    """ возвращает значение из словаря по ключу, если они есть,
        иначе возврашает default - первый из args
    """
    if len(args) == 0:  # default передали?
        default = None
    else:
        default = args[0]

    if key:
        if key in collection.keys():
            return collection[key]
        else:
            return default
    else:
        return default


# print(get_val({"hello": "world"}, "hello"))
# print(get_val({"hello": "world"}, "hello", "python"))
# print(get_val({"hello": "world"}, "", "python"))
# print(get_val({"hello": "world"}, ""))
# print(get_val({}, "hello", "python"))
