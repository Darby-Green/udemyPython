data = [104,101,4,105,308,103,5,107,100,306,106,102,108]

min_val = 100
max_val = 200

# for i in range(len(data)- 1,-1,-1):
#     if data[i] < min_val or data[i] > max_val:
#         print(i,data)
#         del data[i]

top_index = len(data) - 1
for index,value in enumerate(reversed(data)):
    if value < min_val or value > max_val:
        print(top_index - index,value)
        del data[top_index - index]
print(data)

