shopping_list = ["milk", "eggs", "pasta", "spam", "bread", "rice"]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print("adding cream")
shopping_list.append("cream")

print(shopping_list)