from random import randint

def crear_id() -> str:
    id = str(randint(100000, 200000))
    return id