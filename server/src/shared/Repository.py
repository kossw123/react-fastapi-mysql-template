class InMemoryStore:
    def __init__(self):
        self.store = {}

    def save(self, obj):
        print(f"[SAVE] key={obj.id}")
        self.store[obj.id] = obj
        print(self.store)

    def find(self, id):
        print(f"[FIND] key={id}")
        print(self.store)
        return self.store.get(id)

    def delete(self, id):
        del self.store[id]