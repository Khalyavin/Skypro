def calc_salt(arg):
    if isinstance(arg, int):
        return arg / 100
    elif isinstance(arg, str):
        try:
            iarg = int(arg)
        except:
            print(f"invalid literal for int() with base 10: '{arg}'")
            return 0.0
        else:
            return iarg / 100
    else:
        raise ValueError(f"invalid literal for int() with base 10: '{arg}'")
        return 0.0


print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('asd'))
