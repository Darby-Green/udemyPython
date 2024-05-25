data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon","sour, yellow citrus fruit")
]

# print(ord("a"))
# print(ord("b"))
# print(ord("z"))

def simpleHash(s: str) -> int:
    """a very simple hash func"""
    basicHash = ord(s[0])
    return basicHash % 10

def get(k: str) -> str:
    """return the value for a key, or None if the key does not exist"""
    hashCode = simpleHash(k)
    if values[hashCode]:
        return values[hashCode]
    else:
        return None


keys = [""] * 10
values = keys.copy()


for key, value in data:
    h = simpleHash(key)
    print(key, h)
    keys[h] = key
    values[h] = value


print(keys)
print(values)
print()
value = get("lemon")
print(value)