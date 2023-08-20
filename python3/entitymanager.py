from config import config

_next_entity = 0
_entity_pool = set()

def create_entity():
    global _next_entity
    # reuse free'd entities if they are available
    if len(_entity_pool) > 0:
        return _entity_pool.pop()
    else:
        entity = _next_entity
        _next_entity = _next_entity + 1
    return entity


'''Place entities into _entity_pool freeing them up for use by newly created entities.'''


def clear_entities(entity_ids={}):
    _entity_pool.update(entity_ids)
