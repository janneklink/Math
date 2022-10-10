def ggt(a:int,b:int):
    """
    :param a: int
    :param b: int
    :return: int größter gemeinsamer Teiler von a und b
    """
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
    return a