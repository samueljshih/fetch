from uuid import uuid4

store = {}

def save(receipt, points):
    rid = str(uuid4())
    store[rid] = points
    return rid

def retrieve(rid):
    return store.get(rid)
