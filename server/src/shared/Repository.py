class Domain_Repository():
    def __init__(self):
        self.store = {}
    def save(self, obj):
        self.store[obj.id] = obj
    def find(self, id):
        return self.store.get(id)
    def delete(self, id):
        del self.store[id]