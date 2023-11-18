class MyDict(dict):
    def get(self, key):
        return super().get(key, 0)


d = MyDict({"a": 1, "b": 2})
print(d.get("c"))
