shopping = ["milk","bread","eggs","spam","rice"]
item_to_find = "bread"
found_at = None
# for index in range(6)
# for index in range(len(shopping)):
#     if shopping[index] == item_to_find:
#         found_at = index
if item_to_find in shopping:
    found_at=shopping.index(item_to_find) 
if found_at is not None:
    print("Item at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))