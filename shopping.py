shopping = ["milk","bread","eggs","spam","rice"]
# for item in shopping:
#     if item != "bread":
#         print("Buy "+item)

for item in shopping:
    if item == "bread":
        break
    print("Buy "+item)