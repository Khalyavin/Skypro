# файл index_of.py
def index_of(coll, value, from_index=0):
    length = len(coll)

    if length == 0:
        return -1

    index = from_index

    if index < 0:
        if index < -length:
            index = 0
        else:
            index += length

    try:
        return coll.index(value, index)
    except ValueError:
        return -1
