from config import config

_next_entity = 0

def create_entity():
    global _next_entity
    entity = _next_entity
    _next_entity = _next_entity + 1
    return entity
