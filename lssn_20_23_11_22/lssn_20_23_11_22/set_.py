def set_(coll: dict, path: list, value: int):
    """ в словаре coll проходит по пути path и изменяет (добавляет) value
    """
    res = coll
    for ind in range(len(path)):    # побежали по path
        if path[ind] in res.keys():     # ключ есть в пути
            if ind == len(path) - 1:
                res[path[ind]] = value      # конец пути
                return
            else:
                res = res[path[ind]]        # иду глубже
        else:                           # ключа нет в пути
            if ind == len(path) - 1:
                res[path[ind]] = value      # конец пути
                return
            else:
                res[path[ind]] = {}         # добавляю
                res = res[path[ind]]

coll = {"a": {"b": {"c": 3}}}
set_(coll, ["a", "b", "c"], 4)
print(coll["a"]["b"]["c"])
set_(coll, ["x", "y", "z"], 5)
print(coll["x"]["y"]["z"])
print(coll)