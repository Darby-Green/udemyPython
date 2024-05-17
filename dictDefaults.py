from contents import pantry

chickQuantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chickQuantity}")

beansQuantity = pantry.setdefault("beans", 0)
print(f"beans: {beansQuantity}")

catsupQuantity = pantry.get("ketchup", 0)
print(f"ketchup: {catsupQuantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)